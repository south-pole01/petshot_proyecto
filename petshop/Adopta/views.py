from django.shortcuts import render, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, AccessMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Adopta
from .forms import AdoptaForm

from rest_framework import generics, status
from .serializers import AdoptaSerializer

from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AdoptaSerializer
from django.shortcuts import render, redirect, get_object_or_404

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 



class AdoptaList (ListView):                    
    model = Adopta
    template_name = 'Adopta/adopta_list.html'

class AdoptaCreate (CreateView):
    model = Adopta
    form_class = AdoptaForm
    template_name = 'Adopta/adopta_form.html'
    success_url = reverse_lazy('adopta_list')

class AdoptaUpdate(UpdateView):
    model = Adopta
    form_class = AdoptaForm
    template_name = 'Adopta/adopta_form.html'
    success_url = reverse_lazy('adopta_list')

class AdoptaDelete(DeleteView):
    model = Adopta
    template_name = 'Adopta/adopta_borrar.html'
    success_url = reverse_lazy('adopta_list')
    
    
@api_view(['GET', 'POST'])
def adopta_collection(request):
    if request.method == 'GET':
        adopta = Adopta.objects.all()
        serializer = AdoptaSerializer(adopta, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = AdoptaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def adopta_element(request, pk):
    adopta = get_object_or_404(Adopta, id=pk)

    if request.method == 'GET':
        serializer = AdoptaSerializer(adopta)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        adopta.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT': 
        adopta_new = JSONParser().parse(request) 
        serializer = AdoptaSerializer(adopta, data=adopta_new) 
        if serializer.is_valid(): 
            serializer.save() 
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
