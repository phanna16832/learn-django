from django.urls import path
from .  import views

urlpatterns = [
    path(route = 'helloworld/', view= views.helloworld, name='helloworld'),
    path(route = '', view= views.home, name='home')
]
