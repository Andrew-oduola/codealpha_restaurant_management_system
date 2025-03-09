from django.contrib import admin
from .models import Table

# Register your models here.
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'is_occupied', 'location']
    list_filter = ['is_occupied']
    search_fields = ['table_number', 'location']
    list_editable = ['is_occupied']
    list_per_page = 10
    list_display_links = ['table_number']
    list_max_show_all = 100
    # list_select_related = ['location']
    list_display_links = ['table_number']