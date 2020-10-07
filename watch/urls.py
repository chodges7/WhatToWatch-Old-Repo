from . import views
from watch.views import home
from django.contrib.auth import authenticate
from . import views
from django.urls import path, re_path
urlpatterns = [
        path('', home, name='home'),
        path('home/', views.home),
        path('login_view/', views.login_view),
        path('signup/', views.signup, name="signup"),
]
