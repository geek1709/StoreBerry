from django.shortcuts import render, redirect
from django.views.generic import View


class Index(View):
	def get(self,request):
		template_name = 'index.html'
		context = {
		}
		return render(request,template_name,context)