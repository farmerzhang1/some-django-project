from django.shortcuts import render

# Create your views here.
def test1Page(request):
    return render(request, 'fm/test1.html')

def test2Page(request):
    return render(request, 'fm/test2.html')
