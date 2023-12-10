from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Abilities)
class AbilitiesAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'active',
        'type'
    ]
    
@admin.register(Dangerous)
class DangerousAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'pick',
        'life_point'
    ]