from django.shortcuts import render

from .forms import TiendaForm,RegistrationForm

from .models import UserTienda

class Alta(View):
	def get(self,request):
		template_name = 'registration/altaTienda.html'
		form = TiendaForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)