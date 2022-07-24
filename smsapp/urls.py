from django.urls import path
from . import views


#URL Configuration

urlpatterns = [
    path('home/',views.home,name='home'),
    path('submit/',views.twilio,name='submit'),
    path('email/',views.sendemail,name='sendemail'),
]