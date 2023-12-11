from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Robinson)
class AbilitiesAdmin(admin.ModelAdmin):
    list_display = ["name", "active", "type"]


@admin.register(Dangerous)
class DangerousAdmin(admin.ModelAdmin):
    list_display = ["name", "pick", "life_point"]


@admin.register(Boss)
class BossAdmin(admin.ModelAdmin):
    list_display = ["name", "pick", "life_point", "active"]


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ["life_point", "user", "start"]


@admin.register(deckRobinson)
class deckRobinsonAdmin(admin.ModelAdmin):
    list_display = ["card", "value", "game"]


@admin.register(graveRobinson)
class graveRobinsonAdmin(admin.ModelAdmin):
    list_display = ["card", "value", "game"]


@admin.register(deckBoss)
class deckBossAdmin(admin.ModelAdmin):
    list_display = ["card", "game"]
