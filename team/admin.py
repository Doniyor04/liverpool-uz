from django.contrib import admin
from .models import Position, Player, Staff

# Register your models here.


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "position",
        "year",
        "number",
        "country",
        "matches",
        "get_stat_type",
    )


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "position", "image")
