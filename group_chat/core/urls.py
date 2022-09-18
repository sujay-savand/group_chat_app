import os
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name=os.path.join('core', 'login.html')), name='login'),
    path('signout/', auth_views.LogoutView.as_view(), name='logout'),
]