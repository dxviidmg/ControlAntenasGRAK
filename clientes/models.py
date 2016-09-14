from django.db import models

class Cliente(models.Model):
	nombre = models.CharField(max_length=20)
	apellido_materno = models.CharField(max_length=20)
	apellido_paterno = models.CharField(max_length=20)
	telefono = models.CharField(max_length=10)
	mail = models.EmailField(max_length=20)

	def __str__(self):
		return self.nombre

class Direccion(models.Model):
	cliente = models.OneToOneField(Cliente)
	calle = models.CharField(max_length=20)
	numero_exterior = models.CharField(max_length=10)
	numero_interior = models.CharField(max_length=10, blank=True, null=True)
	colonia = models.CharField(max_length=20)
	municipio = models.CharField(max_length=20)
	estado = models.CharField(max_length=20)
	codigo_postal = models.CharField(max_length=5)