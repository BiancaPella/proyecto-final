
from django.urls import path
from .views import CambiarContrasenaView, RegistroUsuarioView, EditarUsuarioView
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('editar_perfil/', EditarUsuarioView.as_view(), name='editar_perfil'),
    path('password/', CambiarContrasenaView.as_view()),
    path('password_success', views.password_success, name='password_success')
    ]