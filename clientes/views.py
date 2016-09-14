from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListClientes(View):
	def get(self, request,):
		template_name = "clientes/listClientes.html"
		clientes = Cliente.objects.all().order_by("apellido_mateṛno", "apellido_mateṛno", "nombre")
		context = {
		'clientes': clientes
		}
		return render(request, template_name, context)