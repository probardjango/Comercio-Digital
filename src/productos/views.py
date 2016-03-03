from django.core.urlresolvers import reverse 
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from comerciodigital.mixins import MultiSlugMixin, SubmitBtnMixin, LoginRequiredMixin

from .forms import ProductoForm, ProductoModelForm
from .mixins import ProductoManagerMixin
from .models import Producto

class ProductoCreateView(LoginRequiredMixin, SubmitBtnMixin, CreateView):
	model = Producto 
	form_class = ProductoModelForm
	template_name = "form.html"
	# success_url = "/productos/crear/"
	submit_btn = "Crear Producto"

	def form_valid(self, form):
		user = self.request.user
		form.instance.user = user
		valid_data = super(ProductoCreateView, self).form_valid(form)
		
		form.instance.managers.add(user)
		return valid_data

	# def get_success_url(self):
	# 	return reverse("producto_list_view")


class ProductoUpdateView(ProductoManagerMixin, SubmitBtnMixin, MultiSlugMixin, UpdateView):
	model = Producto 
	form_class = ProductoModelForm
	template_name = "form.html"
	success_url = "/productos/"
	submit_btn = "Actualizar Producto"


class ProductoDetailView(MultiSlugMixin, DetailView):
	model = Producto

class ProductoListView(ListView):
	model = Producto

	def get_queryset(self, *args, **kwargs):
		qs = super(ProductoListView, self).get_queryset(**kwargs)
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