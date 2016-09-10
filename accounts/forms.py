from .models import UserTienda
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Tu password: ', widget=forms.PasswordInput)
	password1 = forms.CharField(label='Repite tu password: ', widget=forms.PasswordInput)
	class Meta:
		model = User
		fields = ('username','first_name','email')

	def clean_password1(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Tus paswword no coinciden compa')
		return cd['password2']