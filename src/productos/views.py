from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import ProductoForm, ProductoModelForm
from .models import Producto

def create_view(request):
	#FORMulario
	form = ProductoModelForm(request.POST or None)
	if form.is_valid():
		print form.cleaned_data.get("estado")
		instance = form.save(commit=False)
		#codigo
		#instrucciones
		instance.precio_rebajas = instance.precio
		instance.save()


	template = "create_view.html"
	context = {
		"form": form
	}
	return render(request, template, context)

def detail_view(request, objeto_id=None):
	producto = get_object_or_404(Producto, id=objeto_id)
	template = "detail_view.html"
	context = {
		"titulo": "Detail View",
		"objeto": producto
		}
	print objeto_id
	return render(request, template, context)

def update_view(request, objeto_id=None):
	producto = get_object_or_404(Producto, id=objeto_id)
	form = ProductoModelForm(request.POST or None, instance=producto)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		
	template = "update_view.html"
	context = {
		"objeto": producto,
		"form": form,
		}
	return render(request, template, context)



def slug_detail_view(request, slug=None):
	try:
		producto = get_object_or_404(Producto, slug=slug)
	except Producto.MultipleObjectsReturned:
		producto = Producto.objects.filter(slug=slug).order_by("titulo").first()
	template = "detail_view.html"
	context = {
		"titulo": "Detail View",
		"objeto": producto
		}
	return render(request, template, context)




def list_view(request):
	#lista de objetos
	template = "list_view.html"
	queryset = Producto.objects.all()
	context = {
		"queryset": queryset
	}
	print request
	return render(request, template, context)