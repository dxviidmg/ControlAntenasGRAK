from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *

class ListClientes(View):
	def get(self, request,):
		template_name = "clientes/listClientes.html"
		clientes = Cliente.objects.all()
		context = {
		'clientes': clientes,
		}
		return render(request, template_name, context)