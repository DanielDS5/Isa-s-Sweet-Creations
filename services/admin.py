from django.contrib import admin
from .models import cakes

# Register your models here.

class cakesAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "image")

admin.site.register(cakes, cakesAdmin)