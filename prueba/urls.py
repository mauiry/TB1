from django.conf.urls import patterns, include, url

from django.contrib import admin

from compras import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pract.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^personas/',views.listarPersona),
    url(r'^productos/',views.listarProducto),
    url(r'^compras/',views.listarCompra),
)

