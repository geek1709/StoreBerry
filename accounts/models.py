from django.db import models
from django.contrib.auth.models import User

class UserTienda(models.Model):
	nombre_tienda = models.CharField(max_length=140)
	user = models.OneToOneField(User)

	def __str__(self):
		return 'esta tienda le pertenece a {}'.format(self.user)

class UsersNormal(models.Model):
	user = models.OneToOneField(User)
	nombre = models.CharField(max_length=140)
	email = models.CharField(max_length=140)

	def __str__(self):
		return 'este perfil le pertenece a {}'.format(self.user)