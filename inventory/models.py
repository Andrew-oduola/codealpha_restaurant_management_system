from django.db import models

# Create your models here.
class Inventory(models.Model):
    item_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=50)
    reorder_level = models.IntegerField()
    supplier = models.CharField(max_length=100, null=True, blank=True)
    last_ordered = models.DateTimeField(null=True, blank=True)


    def __str__(self):
        return self.item_name
    
    class Meta:
        verbose_name_plural = "Inventory"