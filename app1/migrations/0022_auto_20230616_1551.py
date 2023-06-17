# Generated by Django 3.1.5 on 2023-06-16 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0021_auto_20230420_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sales_voucher_stock_item_allocation',
            name='sales_invoice_id',
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='sale_vou_stk_itm_allo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.sales_voucher_stock_item_allocation'),
        ),
    ]