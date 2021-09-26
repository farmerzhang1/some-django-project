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

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # handle_uploaded_file(request.FILES['file'])
            file_obj = request.FILES['file']

            with default_storage.open('tmp/something.spthy', 'wb+') as destination:
                for chunk in file_obj.chunks():
                    destination.write(chunk)
            process = subprocess.run([settings.BIN_ROOT+'bin', settings.MEDIA_ROOT+'tmp/something.spthy'], capture_output=True)
            output1 = process.stdout
            print(output1)
            print(request.FILES['file'])
            print (form.cleaned_data)
            request.session['temp_data'] = { 'number' : output1.decode('utf8') }
            return redirect('result')
        else:
            print('not valid!!!!')
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'fm/upload.html', {'form': form})

def result(request):
    hello = request.session['temp_data']
    print(hello)
    return render(request, 'fm/result.html', {'number': hello})
