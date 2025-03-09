from django.contrib import admin
from menu.models import MenuCategory, MenuItem

# Register your models here.
@admin.register(MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    pass

