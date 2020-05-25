from django.contrib import admin

from .models import Nemos, Users, UserStocks

admin.site.register(Nemos)
admin.site.register(Users)
admin.site.register(UserStocks)

