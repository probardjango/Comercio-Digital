from django.shortcuts import render

# Create your views here.

def detail_view(request):
	#1 objeto
	template = "detail_view.html"
	context = {}
	print request
	return render(request, template, context)

def list_view(request):
	#lista de objetos
	template = "list_view.html"
	context = {}
	print request
	return render(request, template, context)