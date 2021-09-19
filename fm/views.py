from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import *
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
            print(request.FILES['file'])
            print (form.cleaned_data)
            request.session['temp_data'] = { 'number' : 1234 }
            return redirect('result')
        else:
            print('not valid!!!!')
            print(form.errors)
    else:
        form = UploadFileForm()
    return render(request, 'fm/upload.html', {'form': form})

def result(request):
    print(request.session['temp_data'])
    return render(request, 'fm/result.html', {'number': 1})
