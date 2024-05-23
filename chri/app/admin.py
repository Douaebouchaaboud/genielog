from django.contrib import admin

from .models import Product , Order

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'created', 'updated')
    list_filter = ('available', 'created', 'updated', 'category')
    list_editable = ('price', 'stock', 'available')
    prepopulated_fields = {'slug': ('name',)}
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'created', 'updated', 'paid')
    list_filter = ('paid', 'created', 'updated')
