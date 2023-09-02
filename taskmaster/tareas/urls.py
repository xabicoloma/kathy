from django.contrib import admin
from django.urls import path, include
from . import views
from .views import PostUpdateView

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.listarTarea, name='home'),
    path('crearTarea/', views.crear_posteo, name='crearTarea'),
    path('editarTarea/<pk>/', PostUpdateView.as_view(), name='editarTarea'),
    path('eliminarTarea/<id>/', views.eliminar_posteo, name= 'eliminarTarea'),

]

