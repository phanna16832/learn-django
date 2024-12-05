from django.shortcuts import render, HttpResponse

# Create your views here.
def helloworld(request):
    return render(request, 'helloworld.html')
def home(request):
    return render(request=request, template_name='index.html')