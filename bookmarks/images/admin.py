from django.contrib import admin
from .models import *


@admin.register(Images)
class AdminImages(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'created']
    list_filter = ['created']
