from django.db import models
from django.core.urlresolvers import reverse

class Linea(models.Model):
	descripcion = models.CharField(max_length=20)
	distribuidor = models.CharField(max_length=20)
	ancho_de_banda = models.IntegerField()
	slug_linea = models.SlugField(max_length=30, blank=True,null=True)

	def __str__(self):
		return self.descripcion
	
	def get_absolute_url(self):
		return reverse('infraestructura:detailLineaAndlistCelulas',args=[self.slug_linea])

class Celula(models.Model):
	nombre = models.CharField(max_length=20)
	ubicacion = models.TextField()
	ancho_de_banda = models.IntegerField()
	linea = models.ForeignKey(Linea)
	slug_celula = models.SlugField(max_length=30, blank=True,null=True)

	def __str__(self):
		return self.nombre

	def get_absolute_url(self):
		return reverse('infraestructura:detailCelulaAndListRedesLan',args=[self.slug_celula])

class RedLan(models.Model):
	ip_red = models.GenericIPAddressField()
	ip_host_inicial = models.GenericIPAddressField()
	ip_host_final = models.GenericIPAddressField()
	ip_mascara_de_red = models.GenericIPAddressField()
	celula = models.ForeignKey(Celula)

	def __str__(self):
		return self.ip_red