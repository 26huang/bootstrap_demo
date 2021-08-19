from django.contrib import admin
from .models import Data
# Register your models here.


class DataAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name', {'fields': ['first_name', 'last_name']})
    ]

admin.site.register(Data, DataAdmin)