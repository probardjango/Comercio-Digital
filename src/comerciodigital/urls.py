from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'comerciodigital.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail/(?P<objeto_id>\d+)$', 'productos.views.detail_view', name='detail_view'),
    url(r'^list/$', 'productos.views.list_view', name='list_view'),
]

