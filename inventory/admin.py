from django.contrib import admin
from .models import Inventory
from django.db.models import F

# Register your models here.
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'quantity', 'reorder_level')
    list_filter = ('reorder_level', 'supplier')
    search_fields = ('item_name', 'supplier')
    date_hierarchy = 'last_ordered'
    actions = ['order_more']
    ordering = ('reorder_level',)

    def order_more(self, request, queryset):
        queryset.update(quantity=F('quantity') + 5)
        self.message_user(request, "Orders more items for selected items.")
        return None