from django.contrib import admin

# Register your models here.

from .models import itemclass,userclass

admin.site.register(itemclass)
admin.site.register(userclass)
