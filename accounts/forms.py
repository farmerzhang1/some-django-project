from django.forms import ModelForm
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        #or fields = ['customer', 'product']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    '''def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user'''
class CustomerForm(ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']