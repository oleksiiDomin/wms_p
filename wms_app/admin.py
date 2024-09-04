from django.contrib import admin
from django.contrib.admin import ModelAdmin
from wms_app.models import *



class CoilInline(admin.TabularInline):
    model = Coil
    extra = 1



@admin.register(Seller)
class SellerAdmin(ModelAdmin):
    pass



@admin.register(Calcium)
class CalciumAdmin(ModelAdmin):
    readonly_fields = ('current_balance',)



@admin.register(CalciumSilicon)
class CalciumSiliconAdmin(ModelAdmin):
    readonly_fields = ('current_balance',)



@admin.register(Carbon)
class CarbonAdmin(ModelAdmin):
    readonly_fields = ('current_balance',)



@admin.register(MetalStrip)
class MetalStripAdmin(ModelAdmin):
    readonly_fields = ('current_balance',)



@admin.register(MetalShot)
class MetalShotAdmin(ModelAdmin):
    readonly_fields = ('current_balance',)



@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    inlines = [CoilInline]



@admin.register(Order)
class OrderAdmin(ModelAdmin):
    pass


@admin.register(Coil)
class CoilAdmin(ModelAdmin):
    pass



@admin.register(IncludedMaterial)
class IncludedAdmin(ModelAdmin):
    pass