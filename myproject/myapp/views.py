from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    create_year = 2024
    current_year = datetime.now().year
    year = current_year - create_year
    return render(request, "index.html", {'create_year': create_year,
                                        'year': year})
def login(request):
    return render(request, "login.html")
