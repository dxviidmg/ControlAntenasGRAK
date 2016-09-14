from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from .models import *
from .forms import BusquedaInformacionLineaForm
from django.db.models import Sum

class ListLineas(View):
	def get(self, request):
		template_name = "infraestructura/listLineas.html"
		lineas = Linea.objects.all()
		context = {
		'lineas': lineas,
		}
		return render(request, template_name, context)

class DetailLineaAndListCelulas(View):
	def get(self, request, slug_linea):
		template_name = "infraestructura/detailLinea.html"
		lineas = Linea.objects.all().order_by("descripcion")
		linea = get_object_or_404(Linea, slug_linea=slug_linea)
		celulas = Celula.objects.all().filter(linea=linea)

		MegasTotal = Linea.objects.all().filter( slug_linea=slug_linea).aggregate(MegasTotal=Sum('ancho_de_banda'))['MegasTotal']
		MegasUsados = Celula.objects.all().filter(linea=linea).aggregate(MegasUsados=Sum('ancho_de_banda'))['MegasUsados']
		
		if MegasUsados is None:
			MegasUsados = 0

		MegasDisponibles = MegasTotal - MegasUsados

		context = {
		'lineas': lineas,
		'linea': linea,
		'celulas': celulas,
		'MegasTotal': MegasTotal,
		'MegasUsados': MegasUsados,
		'MegasDisponibles': MegasDisponibles,
		}
		return render(request, template_name, context)

class DetailCelulaListRedesLan(View):
	def get(self, request, slug_celula):
		template_name = "infraestructura/detailCelula.html"
		celulas = Celula.objects.all().order_by("nombre")
		celula = get_object_or_404(Celula, slug_celula=slug_celula)
		redesLan = RedLan.objects.all().filter(celula=celula)

		MegasTotal = Celula.objects.all().filter( slug_celula=slug_celula).aggregate(MegasTotal=Sum('ancho_de_banda'))['MegasTotal']

		MegasDisponibles = MegasTotal

		context = {
		'celulas': celulas,
		'celula': celula,
		'redesLan': redesLan,
		'MegasTotal': MegasTotal,
		'MegasDisponibles': MegasDisponibles,
		}
		return render(request, template_name, context)