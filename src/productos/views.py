from django.shortcuts import render

# Create your views here.
from .models import Producto

def detail_view(request):
	#1 objeto
	if request.user.is_authenticated():
		template = "detail_view.html"
		producto = Producto.objects.all().first()
		context = {
			"titulo": "Detail View",
			"producto": producto
		}
	else :
		template = "no_encontrado.html"
		context = {}

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