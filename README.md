# Comercio-Digital



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