from django.conf.urls import include, url
from django.contrib import admin

from productos.views import (
    ProductoCreateView,
    ProductoDetailView,
    ProductoListView, 
    ProductoUpdateView,
    )

urlpatterns = [
    # Examples:
    # url(r'^$', 'comerciodigital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^create/$', 'productos.views.create_view', name='create_view'),
    url(r'^detail/(?P<objeto_id>\d+)/edit/$', 'productos.views.update_view', name='update_view'),
    url(r'^detail/(?P<objeto_id>\d+)/$', 'productos.views.detail_view', name='detail_view'),
    url(r'^detail/(?P<slug>[\w-]+)/$', 'productos.views.slug_detail_view', name='slug_detail_view'),
    url(r'^list/$', 'productos.views.list_view', name='list_view'),
    url(r'^productos/$', ProductoListView.as_view(), name='producto_list_view'),
    url(r'^productos/crear/$', ProductoCreateView.as_view(), name='producto_create_view'),
    url(r'^productos/(?P<pk>\d+)/editar/$', ProductoUpdateView.as_view(), name='producto_update_view'),
    url(r'^productos/(?P<slug>[\w-]+)/editar/$', ProductoUpdateView.as_view(), name='slug_producto_update_view'),
    url(r'^productos/(?P<pk>\d+)/$', ProductoDetailView.as_view(), name='producto_detail_view'),
    url(r'^productos/(?P<slug>[\w-]+)/$', ProductoDetailView.as_view(), name='slug_producto_detail_view'),

]

