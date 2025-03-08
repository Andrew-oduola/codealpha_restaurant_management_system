# Generated by Django 5.1.7 on 2025-03-08 01:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tables', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('reservation_time', models.DateTimeField()),
                ('party_size', models.IntegerField()),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tables.table')),
            ],
        ),
    ]
