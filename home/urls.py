from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('videos', views.videos, name='videos'),
    path('search', views.search, name='search'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
]