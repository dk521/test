from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Customer._meta.fields]
    class Meta:
        model = Customer


admin.site.register(Customer, CustomerAdmin)