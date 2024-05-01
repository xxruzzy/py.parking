from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register_page/', views.register_page, name='register_page'),
    path('register/', views.register, name='register'),
    path('login_page/', views.login_page, name='login_page'),
    path('user/', views.user, name='user')
]