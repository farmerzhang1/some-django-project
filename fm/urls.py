from django.urls import path
from .views import *;
urlpatterns = [
    path('', mainPage, name = 'main'),
    path('tamarin/', run_tamarin, name='tamarin'),
    path('load_file/', load_file, name='load_file'),
    path('delete_file/', delete_file, name='delete_file'),
    path('add_file/', add_file, name='add_file'),
    path('test2', test2Page, name = 'test2'),
    path('fv_old', sub1, name = 'formal verification old'),
    path('dp', sub2, name = 'defect prediction'),
    path('dd', sub3, name = 'defect detection'),
    path('upload', upload_file, name = 'upload'),
    path('fv', upload_new, name = 'formal verification'),
    path('result', result, name = 'result'),
]
