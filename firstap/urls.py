
from django.urls import path
from django.urls import re_path
from firstap import views

urlpatterns = [
    path('', views.indexk, name='home'),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
]