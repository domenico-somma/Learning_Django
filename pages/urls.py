# pages/urls.py
from django.urls import path

from .views import homePageView,aboutPageView,get_name,helloPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='About me'),
    path('insert_name/', get_name, name='Insert Name'),
    path('hello/', helloPageView, name='Hello'),
#    path('thanks/', namePageView, name='Insert Name'),
]
