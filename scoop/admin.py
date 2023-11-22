from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display =  ['id','name','description','image']
    list_filter = ['name']
    search_fields = ['name']