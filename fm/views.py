from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.files.storage import default_storage
from .forms import *
import subprocess
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
        if form.is_valid():
            if screenshot:
                code = open(settings.MEDIA_ROOT + 'kea_plus_AdvKey.spthy')
                code_str = code.read()
                code_list = code_str.split('\n')
                code_list[:] = [x for x in code_list if x]
                log = open(settings.MEDIA_ROOT + 'kea_plus_AdvKey_result.log')
                log_str = log.read()
                log_list = log_str.split('\n')
                log_list[:] = [x for x in log_list if x]
                request.session['temp_data'] = { 'logs': log_list, 'codes' : code_list, 
                'full_code': code_str, 'full_log': log_str}
            else:
                file_obj = request.FILES['file']

                with default_storage.open('tmp/something.spthy', 'wb+') as destination:
                    for chunk in file_obj.chunks():
                        destination.write(chunk)
                process = subprocess.run(['tamarin-prover', settings.MEDIA_ROOT+'tmp/something.spthy'], capture_output=True)
                output1 = process.stdout
                s = output1.decode('utf-8')
                results = s[s.find('summary of summaries'):].strip('\n').strip('=').split('\n')
                results[:] = [x.strip(' ') for x in results if x]
                results[1] = 'analyzed: ' + request.FILES['file'].name
                request.session['temp_data'] = { 'text' :  results[2:], 'header': results[0], 'filename': results[1]}
            return redirect('result')
        else:
            print('not valid!!!!')
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'fm/upload.html', {'form': form})

def result(request):
    hello = request.session['temp_data']
    # print(hello)
    return render(request, 'fm/result.html', {'result': hello})
