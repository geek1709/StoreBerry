from django.contrib import admin
from .models import UsersNormal,UserTienda

admin.site.register(UserTienda)
admin.site.register(UsersNormal)
