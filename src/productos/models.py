from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
# Create your models here.


class Producto(models.Model):
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(null=True)
	slug = models.SlugField(blank=True) #unique=True
	precio = models.DecimalField(max_digits=50, decimal_places=2, default=9.99) #100.00
	precio_rebajas = models.DecimalField(max_digits=50, decimal_places=2, default=6.99, blank=True, null=True) #100.00


	def __unicode__(self): #Python 3 __str__
		return self.titulo

def producto_pre_save_receptor(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = slugify(instance.titulo)

pre_save.connect(producto_pre_save_receptor, sender=Producto)


# def producto_post_save_receptor(sender, instance, *args, **kwargs):
# 	if instance.slug != slugify(instance.titulo):
# 		instance.slug = slugify(instance.titulo)
# 		instance.save()


# post_save.connect(producto_post_save_receptor, sender=Producto)