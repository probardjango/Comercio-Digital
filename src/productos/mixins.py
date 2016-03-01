from django.http import Http404

from comerciodigital.mixins import LoginRequiredMixin


class ProductoManagerMixin(LoginRequiredMixin, object):
	def get_object(self, *args, **kwargs):
		user = self.request.user
		obj = super(ProductoManagerMixin, self).get_object(*args, **kwargs)
		try:
			obj.user == user
		except:
			raise Http404

		try:
			user in obj.managers.all()
		except: 
			raise Http404

		if obj.user == user or user in obj.managers.all():
			return obj
		else:
			raise Http404