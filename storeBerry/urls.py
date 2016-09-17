
from accounts import urls as cuentasUrls
from tienda import urls as storeUrls
from django.conf.urls import url,include
from django.contrib import admin
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include(cuentasUrls)),
    url(r'^store/',include(storeUrls)),
    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}),
]
