from django.contrib import admin
from .models import *

class MyAdminSite(admin.ModelAdmin):
    search_fields = ["name"]

admin.site.register(Product, MyAdminSite)