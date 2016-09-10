from django.db import models
from django.contrib.auth.models import User

class UserTienda(models.Model):
	nombre_tienda = models.CharField(max_length=140)
	user = models.OneToOneField(User)

	def __str__(self):
		return 'esta tienda le pertenece a {}'.format(self.user)

class UserComprador(models.Model):
	GENEROS = (
		('Hombre','Hombre'),
		('Mujer', 'Mujer'),
		)
	fecha_nacimiento = models.DateField(null=True,blank=True)
	sexo = models.CharField(max_length=140,choices=GENEROS, default="Mujer")
	user = models.OneToOneField(User)

	def __str__(self):
		return 'este perfil le pertenece a {}'.format(self.user)