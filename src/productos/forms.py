from django import forms
from django.utils.text import slugify
from .models import Producto

ESTADO_DE_PRODUCTO = (
	('nuevo', 'Nuevo'),
	('segunda mano', 'Segunda mano'),
	)

class ProductoModelForm(forms.ModelForm):
	estado = forms.ChoiceField(widget= forms.RadioSelect, choices=ESTADO_DE_PRODUCTO, required=False)
	descripcion = forms.CharField(widget=forms.Textarea(
		attrs={
			"placeholder": "Escribir una descripcion de tu producto aqui",
	}))
	
	class Meta: 
		model = Producto
		fields = ["titulo", "descripcion", "precio"]
		# widgets = {
		# 	"descripcion": forms.Textarea(
		# 		attrs={
		# 			"placeholder": "DESCRIPCION!!!!"
		# 		}
		# 	)
		# }

	def clean(self, *args, **kwargs):
		cleaned_data = super(ProductoModelForm, self).clean(*args, **kwargs)
		# titulo = cleaned_data.get("titulo")
		# slug = slugify(titulo)
		# qs = Producto.objects.filter(slug=slug).exists()
		# if qs:
		# 	raise forms.ValidationError("Titulo no disponible, escoge otro por favor.")
		return cleaned_data

	def clean_precio(self):
		precio = self.cleaned_data.get("precio")
		if precio <= 1.00:
			raise forms.ValidationError("Precio tiene que ser mayor que $1.00")
		elif precio > 99.99:
			raise forms.ValidationError("Precio tiene que ser menor que $100.00")
		else:
			return precio

	def clean_titulo(self):
		titulo = self.cleaned_data.get("titulo")
		if len(titulo) > 3:
			return titulo
		else: 
			raise forms.ValidationError("Titulo debe contener mas de 3 caracteres")

class ProductoForm(forms.Form):
	titulo = forms.CharField(label= "Titulo de Producto en Venta", widget=forms.TextInput(
		attrs={
			"class": "other-custom-class",
			"placeholder": "Titulo",
	}))
	descripcion = forms.CharField(widget=forms.Textarea(
		attrs={
			"class": "custom-class",
			"placeholder": "Escribir una descripcion de tu producto aqui",
	}))

	precio = forms.DecimalField()
	estado = forms.ChoiceField(widget= forms.RadioSelect, choices=ESTADO_DE_PRODUCTO, required=False)


	def clean_precio(self):
		precio = self.cleaned_data.get("precio")
		if precio <= 1.00:
			raise forms.ValidationError("Precio tiene que ser mayor que $1.00")
		elif precio > 99.99:
			raise forms.ValidationError("Precio tiene que ser menor que $100.00")
		else:
			return precio


	def clean_titulo(self):
		titulo = self.cleaned_data.get("titulo")
		if len(titulo) > 3:
			return titulo
		else: 
			raise forms.ValidationError("Titulo debe contener mas de 3 caracteres")