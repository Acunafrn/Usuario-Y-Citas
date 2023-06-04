from django.urls import path 
from myapp import views


urlpatterns = [
    path('mysite/', views.mysite, name='mysite'), 
    path('', views.mysite, name='index'),
    path('perfil/', views.perfil, name='perfil'),
]