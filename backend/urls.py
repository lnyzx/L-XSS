from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data/', views.data, name='data'),
    path('auth/', views.auth, name='auth'),
    path('probe/', views.probe, name='probe'),
]