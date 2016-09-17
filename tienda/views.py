from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Product

from .forms import ProductForm




from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Index(View):
	def get(self,request):
		template_name = 'index.html'
		products = Product.objects.all().order_by('nombre_producto')
		context = {
		'products':products
		}
		return render(request,template_name,context)

class ProductLoad(View):
	@method_decorator(login_required)
	def get(self,request):
		template_name = 'loadProduct.html'
		form = ProductForm()
		context = {
			'form':form
		}
		return render(request,template_name,context)
		
	def post(self,request):
		form = ProductForm(request.POST,request.FILES)
		new_product = form.save(commit=False)
		new_product.user = request.user
		new_product.save()
		return redirect('index')