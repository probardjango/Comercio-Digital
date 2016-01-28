from django.db import models

# Create your models here.


class Producto(models.Model):
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(null=True)
	precio = models.DecimalField(max_digits=50, decimal_places=2, default=9.99) #100.00
	precio_rebajas = models.DecimalField(max_digits=50, decimal_places=2, default=6.99, blank=True, null=True) #100.00


	def __unicode__(self): #Python 3 __str__
		return self.titulo

