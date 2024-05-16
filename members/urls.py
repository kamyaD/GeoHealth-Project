# members/urls.py

from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    # Include default authentication URLs
    path('', include('django.contrib.auth.urls')),
]
