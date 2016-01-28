from django.contrib import admin

# Register your models here.

from .models import Producto

class ProductoAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "descripcion", "precio", "precio_rebajas"]
	search_fields = ["titulo", "descripcion"]
	list_filter = ["precio"]
	list_editable = ["precio_rebajas"]
	class Meta:
		model = Producto


admin.site.register(Producto, ProductoAdmin)