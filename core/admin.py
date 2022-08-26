
from django.contrib import admin
# core/admin.py
from core.models import BottleCount
from .models import Bottle

admin.site.register(Bottle)


class BottleCountAdmin(admin.ModelAdmin):
    model = BottleCount
    list_display = ["count", "order1", "bottle", "finished"]
    list_editable = ["order1", "bottle", "finished"]
    fields = ["count", "order1",  "bottle", "finished"]


admin.site.register(BottleCount, BottleCountAdmin)

