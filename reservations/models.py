from django.db import models
from tables.models import Table
from django.utils import timezone

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

    @staticmethod
    def get_available_tables(reservation_time, party_size):
        # Filter tables based on seat capacity
        tables = Table.objects.filter(seats__gte=party_size)
        
        # Exclude tables that are reserved during the given reservation time
        reserved_tables = Reservation.objects.filter(
            reservation_time__lte=reservation_time,
            reservation_time__gte=timezone.now()
        ).values_list('table', flat=True)
        
        available_tables = tables.exclude(id__in=reserved_tables)
        return available_tables