from django.db import models
from tables.models import Table
# from menu.models import MenuItem

# Create your models here.
class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    items = models.ManyToManyField('menu.MenuItem', through='OrderItem')
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    ], default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    special_requests = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Order {self.id} for Table {self.table.table_number}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey('menu.MenuItem', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.quantity}x {self.menu_item.name} for Order {self.order.id}"
    
