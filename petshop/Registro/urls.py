from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from Registro import views

urlpatterns = [

       path('listar_departamento', views.listar_departamentos, name="listar_departamento"),
       
       path('add_departamento', views.DeptoCreate.as_view(), name="add_departamento"),
       path('list_depto/', views.DeptoList.as_view(), name='list_depto'),
       path('edit_depto/<int:pk>', views.DeptoUpdate.as_view(), name='edit_depto'),
       path('del_depto/<int:pk>', views.DeptoDelete.as_view(), name='del_depto'),
       path('prod_list', views.ProdList.as_view(), name='prod_list'),
       
       # api
       path('productos/',  views.producto_collection , name='prod_collection'),
       path('productos/<int:pk>/', views.producto_element ,name='prod_element')


]


urlpatterns = format_suffix_patterns(urlpatterns)