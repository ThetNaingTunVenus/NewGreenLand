from django.contrib import admin
from .models import *
# Register your models here.
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'BuyerName','Address')
admin.site.register(Buyer,BuyerAdmin)

class StyleAdmin(admin.ModelAdmin):
    list_display = ('id', 'BuyerName','Address')
admin.site.register(Style,StyleAdmin)

class ProductionLineAdmin(admin.ModelAdmin):
    list_display = ('id', 'BuyerName','Address')
admin.site.register(ProductionLine,ProductionLineAdmin)