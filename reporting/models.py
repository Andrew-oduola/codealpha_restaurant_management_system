from django.db import models
from orders.models import Order

# Create your models here.
class SalesReport(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_orders = models.IntegerField()

    def __str__(self):
        return f"Sales Report for {self.date}"

class InventoryReport(models.Model):
    date = models.DateField()
    item_name = models.CharField(max_length=100)
    quantity_used = models.IntegerField()
    quantity_remaining = models.IntegerField()

    def __str__(self):
        return f"Inventory Report for {self.item_name} on {self.date}"
    
