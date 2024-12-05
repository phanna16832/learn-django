from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>hello world</h1>')

def h1(request):
    return render(request=request, template_name='index.html')