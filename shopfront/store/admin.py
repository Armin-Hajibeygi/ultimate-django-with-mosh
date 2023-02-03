from django.contrib import admin
from . import models

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_stats', 'collection_titles']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']
    
    def collection_titles(self, product):
        return product.collection.title
    
    @admin.display(ordering='inventory')
    def inventory_stats(self, product):
        if product.inventory < 10:
            return 'Low'
        return 'OK' 
    

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']


admin.site.register(models.Collection)
