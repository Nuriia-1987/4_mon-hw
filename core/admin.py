
from django.contrib import admin

from core.models import BottleCount, Bottle


class BottleAdmin(admin.ModelAdmin):
    model = Bottle
    list_display = ['maker', 'volume', 'expired']
    list_editable = ['expired']
    fields = ['maker', 'volume', 'description', 'expired']


admin.site.register(Bottle, BottleAdmin)


class BottleCountAdmin(admin.ModelAdmin):
    model = BottleCount
    list_display = ["count", "order", "bottle", "finished"]
    list_editable = ["order", "bottle", "finished"]
    fields = ["count", "order",  "bottle", "finished"]


admin.site.register(BottleCount, BottleCountAdmin)

