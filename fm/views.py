from django.core.files.base import ContentFile
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.files.storage import default_storage
from .forms import *
import subprocess
from os import listdir
from os.path import isfile, join
from django.conf import settings
# Create your views here.
def mainPage(request):
    return render(request, 'fm/main.html')

def test2Page(request):
    return render(request, 'fm/test2.html')

def sub1(request):
    return render(request, 'fm/1.html')

def sub2(request):
    return render(request, 'fm/2.html')

def sub3(request):
    return render(request, 'fm/3.html')

screenshot = False

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
    else:
        form = UploadFileForm()
    return render(request, 'fm/upload.html', {'form': form})

def upload_new(request):
    tamarin_path = join(settings.MEDIA_ROOT, 'tamarin')
    flist = [(f[:-6], f[:-6].upper()) for f in listdir(tamarin_path)]
    if request.method == 'POST':
        form = UploadFileForm(flist, request.POST, request.FILES)
    else:
        form = UploadFileForm(flist)
    return render(request, 'fm/upload_new.html', {'form': form})

def result(request):
    hello = request.session['temp_data']
    hello["list"] = ["one", "two", "three"]
    # print(hello)
    return render(request, 'fm/result.html', hello)

def run_tamarin(request):
    data = {'msg': ''}
    if request.method == 'GET':
        buffer = request.GET.get('buf')
        # print(buffer)
        path = 'tmp/something.spthy'
        default_storage.delete(path)
        path = default_storage.save(path, ContentFile(buffer))
        # print(path)
        process = subprocess.run(['tamarin-prover', settings.MEDIA_ROOT+path], capture_output=True)
        output1 = process.stdout
        s = output1.decode('utf-8')
        # print(s)
        if s.find('All well-formedness checks were successful') != -1:
            data['msg'] = '成功\n'
        else:
            data['msg'] = '语法错误\n'
        # results = s[s.find('summary of summaries'):].strip('\n').strip('=').split('\n')
        # results[:] = [x.strip(' ') for x in results if x]
        # data['msg'] = request.FILES['file'].name
        # data['msg'] = s
        return JsonResponse(data)

    return JsonResponse(data)

def load_file(request):
    data = {'file' : ''}
    if request.method == 'GET':
        filename = request.GET.get('filename')
        path = 'tamarin/' + filename + '.spthy'
        str = default_storage.open(path).read().decode('utf-8')
        data['file'] = str
        # print(str)
        return JsonResponse(data)
    return JsonResponse(data)

def delete_file(request):
    data = {'success': False}
    if request.method == 'GET':
        filename = request.GET.get('filename')
        path = 'tamarin/' + filename + '.spthy'
        if (filename not in default_files):
            default_storage.delete(path)
            print('deleted! '+path)
            data['success'] = True
            # return redirect(upload_new)
            return JsonResponse(data)
    return JsonResponse(data)

def add_file(request):
    if request.method == 'GET':
        filename = request.GET.get('filename')
        text = request.GET.get('text')
        path = 'tamarin/' + filename # assume it's spthy file, reject in javascript if not
        default_storage.delete(path)
        default_storage.save(path, ContentFile(text))
        # return redirect(upload_new)
    return JsonResponse({})
