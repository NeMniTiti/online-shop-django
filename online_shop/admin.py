from django.contrib import admin

from online_shop.models import Product, Category



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ('title',)
    list_display = ('title',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'price', 'description', 'category',)
    list_display = ('title',)
    list_filter = ('title',)



