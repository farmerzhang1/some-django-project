from django.urls import path
from .views import *;
urlpatterns = [
    path('test1', test1Page, name = 'test1'),
    path('test2', test2Page, name = 'test2'),
    path('fv', sub1, name = 'formal verification'),
    path('dp', sub2, name = 'defect prediction'),
    path('dd', sub3, name = 'defect detection')
]