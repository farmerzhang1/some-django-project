from django.urls import path
from .views import *;
urlpatterns = [
    path('test1', test1Page),
    path('test2', test2Page),
]