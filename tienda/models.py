from django.db import models
from django.contrib.auth.models import User




class Product(models.Model):
	user = models.ForeignKey(User, related_name='product')
	fecha = models.DateTimeField(auto_now=True)
	nombre_producto = models.CharField(max_length=140)
	precio = models.CharField(max_length=140)
	imagen = models.ImageField(upload_to="files", blank = True, null = True)
	

	def __str__(self):
		return 'este producto le pertenece a {}'.format(self.user)
