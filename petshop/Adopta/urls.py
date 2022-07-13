from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import AdoptaList, AdoptaCreate, AdoptaUpdate , AdoptaDelete
from Adopta import views

urlpatterns = [
    path('listar/', AdoptaList.as_view(), name="adopta_list"),

    path('crear/', AdoptaCreate.as_view(), name="adopta_form"),
    path('editar/<int:pk>', AdoptaUpdate.as_view(), name="adopta_update"),
    path('borrar/<int:pk>', AdoptaDelete.as_view(), name="adopta_borrar"),
    
    
    # api
    path('adopcion/',  views.adopta_collection , name='adopta_collection'),
    path('adopcion/<int:pk>/', views.adopta_element ,name='adopta_element')

    
]
