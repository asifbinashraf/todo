from django.urls import path
from . import views

urlpatterns = [

    path('createAccount',views.signup),
    path('index',views.index),
    path('login', views.login),
]