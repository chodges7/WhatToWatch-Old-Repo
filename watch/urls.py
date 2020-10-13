from django.contrib.auth import authenticate
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

from . import views


urlpatterns = [
        path('', views.blank, name='blank'),
        path('home/', views.home),
        path('login/', views.login_view),
        path('signup/', views.signup, name="signup"),
        path('logout/', views.logout_view, name="logout"),
        path('profilePage/', views.profile_view, name="profile"),
]
