from django.conf.urls import url
from . import views
from django.contrib.auth import views as djangoViews


urlpatterns = [
	url(r'^altausuario/$', views.Alta.as_view(), name="alta"),
	url(r'^profile/$', views.Perfil.as_view(), name="perfil"),
	url(r'^home/$', views.Home.as_view(), name="inicio"),
	url(r'^login/$', djangoViews.login, name="login"),
	url(r'^logout/$', djangoViews.logout, name="logout"),
	
]