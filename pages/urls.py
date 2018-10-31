# pages/urls.py
from django.urls import path

from .views import homePageView,aboutPageView,insert_name,insert_name_plot,helloPageView,plotView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='About me'),
    path('insert_name_hello/', insert_name, name='Insert Name'),
    path('insert_name_plot/', insert_name_plot, name='Insert Name'),
    path('hello/', helloPageView, name='Hello'),
    path('plot/', plotView, name='Plot'),
]
