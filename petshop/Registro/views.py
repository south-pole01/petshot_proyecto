from django.shortcuts import render, redirect
from Registro.models import Departamento
from Registro.models import Producto
from .forms import DeptoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



def listar_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, "Registro/listar_departamentos.html", {'Departamentos': departamentos})


# --GEnerics Generics -------
class DeptoCreate(CreateView):
    model = Departamento
    form_class = DeptoForm
    template_name = 'Registro/depto_form.html'
    success_url = reverse_lazy("list_depto")
    
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



class ProdList(ListView):
    model = Producto
    template_name = 'Registro/list_prod.html'
    


#------------- importacines API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductoSerializer
from django.shortcuts import render, redirect, get_object_or_404




@api_view(['GET', 'POST'])
def producto_collection(request):
    if request.method == 'GET':
        productos = Producto.objects.all()
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def producto_element(request, pk):
    producto = get_object_or_404(Producto, id=pk)

    if request.method == 'GET':
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        producto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        carrera_new = JSONParser().parse(request) 
        serializer = ProductoSerializer(producto, data=carrera_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





