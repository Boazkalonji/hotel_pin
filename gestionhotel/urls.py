
from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'gestionhotel'

urlpatterns = [

    path('index', index , name='index'),
    path('about', about , name='about'),
    path('galerie', galerie , name='galerie'),
    path('album1', album1 , name='album1'),
    path('album2', album2 , name='album2'),
    path('contact', contact , name='contact'),

]