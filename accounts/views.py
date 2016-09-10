from django.shortcuts import render
from django.views.generic import View
from .forms import TiendaForm,RegistrationForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


from .models import UserTienda

class Alta(View):
	def get(self,request):
		template_name = 'registration/altaTienda.html'
		form = RegistrationForm
		context = {
		'form':form,
		}
		return render(request,template_name,context)

class Perfil(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'accounts/perfil.html'
		context = {}
		return render(request, template_name, context)
