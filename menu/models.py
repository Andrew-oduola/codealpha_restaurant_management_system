from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_category_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Menu Categories'

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(MenuCategory, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True)


    def __str__(self):
        return self.name
    
# TODO 1: Create a model called Category
# TODO 2: Create a model called
