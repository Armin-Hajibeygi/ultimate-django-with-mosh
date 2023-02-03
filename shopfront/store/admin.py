from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html, urlencode
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


@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'products_count']
    
    @admin.display(ordering='products_count')
    def products_count(self, collection):
        #app_model_page
        url = (
            reverse('admin:store_product_changelist') 
            + '?'
            + urlencode({
                'collection__id': str(collection.id)
            }))
        return format_html('<a href="{}">{}</a>', url, collection.products_count)
        
    
    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            products_count=Count('product')
        )
