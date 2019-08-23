from django.contrib import admin
from m2m.models import Plant, Characteristic

class PlantAdmin(admin.ModelAdmin):
    pass


admin.site.register(Plant, PlantAdmin)
