from django.urls import path
from .  import views

urlpatterns = [
    path(route = '', view= views.home, name='home'),
    path(route = 'h1/', view= views.h1, name='h1')
]
