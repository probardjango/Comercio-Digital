from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .forms import ProductoForm, ProductoModelForm
from .models import Producto

class ProductoDetailView(DetailView):
	model = Producto

	def get_object(self, *args, **kwargs):
		slug = self.kwargs.get("slug")
		ModelClass = self.model
		if slug is not None:
			try:
				obj = get_object_or_404(ModelClass, slug=slug)
			except ModelClass.MultipleObjectsReturned:
				obj = ModelClass.objects.filter(slug=slug).order_by("titulo").first()
		else:
			obj = super(ProductoDetailView, self).get_object(*args, **kwargs)
		return obj 

class ProductoListView(ListView):
	model = Producto
	# template_name = "list_view.html"

	# def get_context_data(self, **kwargs):
	# 	context = super(ProductoListView, self).get_context_data(**kwargs)
	# 	print context
	# 	context["queryset"] = self.get_queryset()
	# 	return context

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductoListView, self).get_queryset(**kwargs)
		# qs = qs.filter(titulo__icontains="sandwhich")
		return qs

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


	template = "form.html"
	context = {
		"form": form,
		"submit_btn": "CREARRR PRODUCTO"
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
		
	template = "form.html"
	context = {
		"objeto": producto,
		"form": form,
		"submit_btn": "ACTUALIZARRR PRODUCTO"
		}
	return render(request, template, context)



def slug_detail_view(request, slug=None):
	producto = Producto.objects.get(slug=slug)
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