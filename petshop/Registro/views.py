from django.shortcuts import render, redirect
from Registro.models import Departamento
from .forms import DeptoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, "Registro/listar_departamentos.html", {'Departamentos': departamentos})


# --GEnerics Generics -------
class DeptoCreate(CreateView):
    model = Departamento
    form_class = DeptoForm
    template_name = 'Registro/depto_form.html'
    success_url = reverse_lazy("listar_departamentos")
    
class DeptoList(ListView):
    model = Departamento
    template_name = 'Registro/list_depto.html'
    # paginate_by = 4

class DeptoUpdate(UpdateView):
    model = Departamento
    form_class = DeptoForm
    template_name = 'Registro/depto_form.html'
    success_url = reverse_lazy('list_depto')

class DeptoDelete(DeleteView):
    model = Departamento
    template_name = 'Registro/depto_delete.html'
    success_url = reverse_lazy('list_depto')




