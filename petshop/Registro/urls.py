from django.urls import path, include
from . import views

urlpatterns = [

       path('add_departamento', views.DeptoCreate.as_view(), name="add_departamento"),
       path('list_depto/', views.DeptoList.as_view(), name='list_depto'),
       path('edit_depto/<int:pk>', views.DeptoUpdate.as_view(), name='edit_depto'),
       path('del_depto/<int:pk>', views.DeptoDelete.as_view(), name='del_depto'),



]
