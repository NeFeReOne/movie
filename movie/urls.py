from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'movie'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),   
    path('', views.index, name='index'),
    path('time', views.time, name='time'),
    path('feel', views.feel, name='feel'),
    path('hobby', views.hobby, name='hobby'),
    path('interest', views.interest, name='interest'),
    path('result', views.result, name='result'),
]