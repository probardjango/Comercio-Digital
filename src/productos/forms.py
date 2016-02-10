from django import forms


class ProductoForm(forms.Form):
	titulo = forms.CharField()
	descripcion = forms.CharField()
	precio = forms.DecimalField()

	