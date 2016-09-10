from django.shortcuts import render
from django.views.generic import View
from .forms import TiendaForm,RegistrationForm

from .models import UserTienda

class Alta(View):
	def get(self,request):
		template_name = 'registration/altaUsuario.html'
		form = RegistrationForm
		context = {
		'form':form,
		}
		return render(request,template_name,context)
