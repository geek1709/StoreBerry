
from accounts import urls as cuentasUrls
from tienda import urls as storeUrls
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/',include(cuentasUrls)),
    url(r'^store/',include(storeUrls)),
]
