from django.db import models

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Table {self.table_number}"

