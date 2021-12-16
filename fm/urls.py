from django.urls import path
from .views import *;
urlpatterns = [
    path('', mainPage, name = 'main'),
    path('tamarin/', run_tamarin, name='tamarin'),
    path('load_file/', load_file, name='load_file'),
    path('test2', test2Page, name = 'test2'),
    path('fv', sub1, name = 'formal verification'),
    path('dp', sub2, name = 'defect prediction'),
    path('dd', sub3, name = 'defect detection'),
    path('upload', upload_file, name = 'upload'),
    path('upload_new', upload_new, name = 'upload_new'),
    path('result', result, name = 'result'),
]
