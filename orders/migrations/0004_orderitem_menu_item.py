# Generated by Django 5.1.7 on 2025-03-12 18:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_menucategory_options'),
        ('orders', '0003_remove_order_items_remove_orderitem_menu_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='menu_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.menuitem'),
            preserve_default=False,
        ),
    ]
