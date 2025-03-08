from django.db import models
from tables.models import Table

# Create your models here.
class Reservation(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=15, null=True, blank=True)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    reservation_time = models.DateTimeField()
    party_size = models.IntegerField()
    special_requests = models.TextField(null=True, blank=True)


    def __str__(self):
        return f"Reservation for {self.customer_name} at {self.reservation_time}"

