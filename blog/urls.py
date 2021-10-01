from django.contrib import admin
from django.urls import path, include
from blog import views
import blog

urlpatterns = [
    path('', views.home, name='home'),
    path('bloghome/', views.bloghome, name='bloghome'),
    path('blogpost/<str:slug>', views.blogpost, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('search/', views.search, name='search'),

]
