from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import CambiarContrasenaForm, EditarPerfilForm, SignUpForm
from django.contrib.auth.views import PasswordChangeView

class RegistroUsuarioView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class EditarUsuarioView(generic.UpdateView):
    form_class = EditarPerfilForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('posts')

    def get_object(self):
        return self.request.user

class CambiarContrasenaView(PasswordChangeView):
    form_class = CambiarContrasenaForm
    template_name = 'registration/cambiar_contrasena.html'
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})