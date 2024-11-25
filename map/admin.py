from django.contrib import admin
from .models import Location

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("address", "city", "latitude", "longitude", "created_at")
    search_fields = ("address", "city")