# Generated by Django 3.1.5 on 2023-03-22 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0016_auto_20230322_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='rate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
