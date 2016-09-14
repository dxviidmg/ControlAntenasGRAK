from django.conf.urls import url
from . import views

urlpatterns = [
 	url(r'^clientes', views.ListClientes.as_view(),name="listClientes"),
]