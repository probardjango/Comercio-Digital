from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Producto

def detail_view(request, objeto_id=None):
	producto = get_object_or_404(Producto, id=objeto_id)
	template = "detail_view.html"
	context = {
		"titulo": "Detail View",
		"objeto": producto
		}
	return render(request, template, context)


	# 	try:
	# 		producto = Producto.objects.get(id=objeto_id)

	# 	except Producto.DoesNotExist:
	# 		producto = None
	# else:
	# 	raise Http404
	#1 objeto
	# if request.user.is_authenticated():

	# else :
	# 	template = "no_encontrado.html"
	# 	context = {}



def list_view(request):
	#lista de objetos
	template = "list_view.html"
	queryset = Producto.objects.all()
	context = {
		"queryset": queryset
	}
	print request
	return render(request, template, context)