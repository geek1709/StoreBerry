from .models import UserTienda
from django import forms
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Tu password: ', widget=forms.PasswordInput)
	password1 = forms.CharField(label='Repite tu password: ', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','first_name','email')

	def clean_password1(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password1']:
			raise forms.ValidationError('Tus passwword no coinciden')
		return cd['password1']

class TiendaForm(forms.ModelForm):
	password = forms.CharField(label='Tu password: ', widget=forms.PasswordInput)
	password1 = forms.CharField(label='Repite tu password: ', widget=forms.PasswordInput)
	class Meta:
		model = UserTienda
		fields = ['nombre_tienda','user']

	def clean_password1(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password1']:
			raise forms.ValidationError('Tus password no coinciden')
		return cd['password1']