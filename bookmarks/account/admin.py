from django.contrib import admin
from .models import *


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'day_of_birth', 'photo']
    raw_id_fields = ['user']
