from django.contrib import admin

from .models import Order, Filament, FilamentBrand, FilamentMaterialType

# Register your models here.

admin.site.register(Order)
admin.site.register(Filament)
admin.site.register(FilamentBrand)
admin.site.register(FilamentMaterialType)
