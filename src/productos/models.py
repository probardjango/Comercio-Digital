from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils.text import slugify
# Create your models here.


class Producto(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL)
	managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers_productos", blank=True)
	#user = models.OneToOneField(settings.AUTH_USER_MODEL)
	titulo = models.CharField(max_length=120)
	descripcion = models.TextField(null=True)
	slug = models.SlugField(blank=True, unique=True) 
	precio = models.DecimalField(max_digits=50, decimal_places=2, default=9.99) #100.00
	precio_rebajas = models.DecimalField(max_digits=50, decimal_places=2, default=6.99, blank=True, null=True) #100.00

	
	def __unicode__(self): #Python 3 __str__
		return self.titulo

	def get_absolute_url(self):
		view_name = "slug_producto_detail_view"
		return reverse(view_name, kwargs={"slug": self.slug})

def create_slug(instance, new_slug=None):
	slug = slugify(instance.titulo)
	if new_slug is not None:
		slug = new_slug
	qs = Producto.objects.filter(slug=slug)
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def producto_pre_save_receptor(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)

pre_save.connect(producto_pre_save_receptor, sender=Producto)


# def producto_post_save_receptor(sender, instance, *args, **kwargs):
# 	if instance.slug != slugify(instance.titulo):
# 		instance.slug = slugify(instance.titulo)
# 		instance.save()


# post_save.connect(producto_post_save_receptor, sender=Producto)