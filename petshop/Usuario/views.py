from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import RegistroForm


class RegistroUsuario(CreateView):
    model = User
    template_name = "Usuario/usuario_form.html"
    form_class = RegistroForm
    success_url = reverse_lazy('home')
 
 
class UserList(ListView):
    model = User
    template_name = 'Usuario/list_user.html'
