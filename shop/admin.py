from django.contrib import admin
from django.contrib.auth.models import User, Group

from shop.models import Category, Product, Comment, Order

# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.register(Comment)
admin.site.register(Order)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    fields = ('title',)

    # prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'image', 'is_expensive')
    list_filter = ('category',)

    def is_expensive(self, obj):
        return obj.price > 10_000

    is_expensive.boolean = True
