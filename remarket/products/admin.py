from django.contrib import admin
from products.models import Category, Product, ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'seller', 'condition',
                    'location', 'availability', 'delivery_option',)
    list_filter = ('condition', 'location', 'availability', 'delivery_option',)
    search_fields = ('title', 'description',)


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('image', 'product',)
    list_filter = ('product',)
