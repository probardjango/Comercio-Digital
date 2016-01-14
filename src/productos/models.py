from django.db import models

# Create your models here.


class Producto(models.Model):
	titulo = models.CharField(max_length=120)


	def __unicode__(self): #Python 3 __str__
		return self.title

