from django.urls import path
from . import views

urlpatterns = [
    path("", views.landing),
    path('Login/', views.login),
    path('Logout/', views.logout),
    path('Sign_up/', views.Sign_up),
]