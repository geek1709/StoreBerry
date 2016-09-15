from django.shortcuts import render, redirect
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

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

	def post(self,request):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			new_user = form.save(commit=False)
			new_user.set_password(form.cleaned_data['password'])
			new_user.save()
			return redirect('altaTienda')
		else:
			context = {
			'form':form,
			}
			template_name = 'accounts/altaUsuario.html'
			return render(request,template_name,context)
