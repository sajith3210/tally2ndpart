# Generated by Django 3.1.5 on 2023-03-22 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20230322_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='amount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='per',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='quantity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='rate',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
