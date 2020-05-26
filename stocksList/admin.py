from django.contrib import admin

from .models import Nemos, Users, StocksList

admin.site.register(Nemos)
admin.site.register(Users)
admin.site.register(StocksList)

