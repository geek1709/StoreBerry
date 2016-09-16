from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
	url(r'^altausuario/$', views.Alta.as_view(), name="altausuario"),
	url(r'^altatienda/$', views.AltaTienda.as_view(), name="altaTienda"),
	url(r'^login/$', djangoViews.login, name="login"),
	url(r'^logout/$', djangoViews.logout, name="logout"),
]