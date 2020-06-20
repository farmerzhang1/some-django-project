from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *
from .forms import *
from .filters import OrderFilter
from .decorators import *
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.utils.decorators import method_decorator
from django.views.generic import View
'''
@login_required(login_url = 'login')
@admin_only
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {
		'orders':orders,
		'customers':customers,
		'total_orders':total_orders,
		'delivered':delivered,
		'pending':pending
	}
	return render(request, 'accounts/dashboard.html', context)
'''

@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
@method_decorator(admin_only, name = 'dispatch')
class Home(View):
	def get(self, request):
		orders = Order.objects.all()
		customers = Customer.objects.all()

		total_customers = customers.count()

		total_orders = orders.count()
		delivered = orders.filter(status='Delivered').count()
		pending = orders.filter(status='Pending').count()

		context = {
			'orders':orders,
			'customers':customers,
			'total_orders':total_orders,
			'delivered':delivered,
			'pending':pending
		}
		return render(request, 'accounts/dashboard.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer'])
def userPage(request):
	print(request.user.customer)
	orders = request.user.customer.order_set.all()
	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()
	context = {
		'orders':orders,
		'total_orders':total_orders,
		'delivered':delivered,
		'pending':pending
	}
	print(orders)
	return render(request, 'accounts/user.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def products(request):
	products = Product.objects.all()
	context = {
		'products': products
	}
	#return HttpResponse('test')
	return render(request, 'accounts/products.html', context)

'''
@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def customer(request, id):
	customer = get_object_or_404(Customer, id = id)
	orders = customer.order_set.all()
	total_orders = orders.count()
	filter = OrderFilter(request.GET, queryset = orders)
	orders = filter.qs#???

	context = {
		'customer': customer,
		'orders': orders,
		'total_orders': total_orders,
		'filter': filter,
	}
	return render(request, 'accounts/customer.html', context)
'''

@method_decorator(login_required(login_url = 'login'), name = 'dispatch')
@method_decorator(allowed_users(allowed_roles = ['admin']), name = 'dispatch')
class CustomerView(View):
	def get(self, request, *args, **kwargs):
		id = self.kwargs['id']
		customer = get_object_or_404(Customer, id = id)
		orders = customer.order_set.all()
		total_orders = orders.count()
		filter = OrderFilter(request.GET, queryset = orders)
		orders = filter.qs#???

		context = {
			'customer': customer,
			'orders': orders,
			'total_orders': total_orders,
			'filter': filter,
		}
		return render(request, 'accounts/customer.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['customer', 'admin'])
def accountSettings(request):
	form = CustomerForm(instance=request.user.customer)
	context = { 'form': form }
	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES, instance=request.user.customer)
		if form.is_valid():
			form.save()
	return render(request, 'accounts/account_settingsss.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def createOrder(request, id):
	OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 3)
	customer = get_object_or_404(Customer, id = id)
	formset = OrderFormSet(queryset = Order.objects.none(), instance=customer)
	#form = OrderForm(request.POST or None, initial={'customer': customer})

	if request.method == 'POST':
		#form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('home')
	context = {
		'formset': formset,
	}
	return render(request, 'accounts/orderform.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def updateOrder(request, id):
	#to debug
	OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 1)
	customer = Order.objects.get(id = id).customer
	formset = OrderFormSet(instance=customer)
	context = { 'formset': formset }
	if request.method == 'POST':
		formset = OrderFormSet(instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('home')
	return render(request, 'accounts/orderform.html', context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles = ['admin'])
def deleteOrder(request, id):
	order = get_object_or_404(Order, id = id)
	form = OrderForm(instance=order)
	context = { 'order': order }
	if request.method == 'POST':
		order.delete()
		return redirect('home')
	return render(request, 'accounts/delete.html', context)

@unauthenticated_user
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(request, username = username, password = password)
		if user is not None:
			print('login successful')
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username or password incorrect')
	context = {}
	return render(request, 'accounts/login.html', context)

@unauthenticated_user
def registerPage(request):
	user_form = CreateUserForm()
	context = {
		'user_form': user_form,
	}
	if request.method == 'POST':
		user_form = CreateUserForm(request.POST)
		if user_form.is_valid():
			user = user_form.save()
			username = user_form.cleaned_data.get('username')
			'''
			group = Group.objects.get(name = 'customer')
			user.groups.add(group)
			Customer.objects.create(
				user = user,
				name = username
			)'''
			messages.success(request, 'Account ' + username + ' created')
			return redirect('login')
		else:
			print('not valid')
			print(customer_form.errors)
	return render(request, 'accounts/register.html', context)

def logoutPage(request):
	if request.user.is_authenticated:
		logout(request)
		return redirect('login')
	else:
		return redirect('home')