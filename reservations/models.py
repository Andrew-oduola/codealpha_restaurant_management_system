from django.db import models
from tables.models import Table

# Create your models here.
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    party_size = models.IntegerField()

    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"

