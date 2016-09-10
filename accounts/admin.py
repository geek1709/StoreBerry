from django.contrib import admin
from .models import UserComprador,UserTienda

admin.site.register(UserTienda)
admin.site.register(UserComprador)
