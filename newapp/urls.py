from . import views

from django.urls import path
app_name='newapp'
urlpatterns = [
     path('register', views.register, name='register'),
     path('login', views.login, name='login'),
     path('logout', views.login, name='logout'),
     path('detail', views.detail, name='detail'),
     path('new', views.new, name='new'),
     path('msg', views.msg, name='msg'),


]
