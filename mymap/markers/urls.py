from django.http import HttpResponse, HttpResponseRedirect
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        ]
