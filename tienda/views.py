from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Product

from .forms import ProductForm


from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Index(View):
	def get(self,request):
		template_name = 'index.html'
		context = {
		}
		return render(request,template_name,context)

class ProductLoad(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'loadProduct.html'
		form = ProductForm
		context = {
			'form':form
		}
		return render(request,template_name,context)