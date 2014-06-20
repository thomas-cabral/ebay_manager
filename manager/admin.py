from django.contrib import admin
from .models import Item, Category, Image
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Item Details', {
            'fields': ('category', 'name', 'purchased_for', 'description', 'item_weight', 'user')
        }),
        ('Auction Posted', {
            'fields': ('listing_url', 'starting_bid', 'buy_it_now', 'shipping_estimate')
        }),
        ('Item Sold', {
            'fields': ('is_sold', 'sold_for', 'shipping_actual', 'total_weight')
        }),
    )
admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(Category, CategoryAdmin)


class ImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(Image, ImageAdmin)