from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
	nombre_producto = models.CharField(max_length=140)
	precio = models.DecimalField(max_digits=6, decimal_places=4)
	imagen = models.ImageField(upload_to="files", blank = True, null = True)
	user = models.OneToOneField(User)

	def __str__(self):
		return 'este producto le pertenece a {}'.format(self.user)
