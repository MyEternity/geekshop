from django.contrib import admin

from products.models import ProductCategory, Product

# Register your models here.
admin.site.register(ProductCategory)


# admin.site.register(Product)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # отображение админки.
    list_display = ('name', 'price', 'quantity', 'category')
    # дает объект
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    # только чтение
    readonly_fields = ('description',)
    # сортировка
    ordering = ('name', 'price')
    # поиск
