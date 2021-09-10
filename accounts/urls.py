from django.urls import path
from .views import *;

urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('products/', products, name = 'products'),
    path('customer/<int:id>', CustomerView.as_view(), name = 'customer'),
    path('create_order/<int:id>', createOrder, name = 'create_order'),
    path('update_order/<int:id>', updateOrder, name = 'update_order'),
    path('delete_order/<int:id>', deleteOrder, name = 'delete_order'),
    path('login/', loginPage, name = 'login'),
    path('register/', registerPage, name = 'register'),
    path('logout/', logoutPage, name = 'logout'),
    path('user/', userPage, name = 'user-page'),
    path('account/', accountSettings, name = 'account-settings'),
]
