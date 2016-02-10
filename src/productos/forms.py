from django import forms

ESTADO_DE_PRODUCTO = (
	('nuevo', 'Nuevo'),
	('segunda mano', 'Segunda mano'),
	)

class ProductoForm(forms.Form):
	titulo = forms.CharField()
	descripcion = forms.CharField(widget=forms.Textarea)
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