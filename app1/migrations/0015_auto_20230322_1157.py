# Generated by Django 3.1.5 on 2023-03-22 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20230215_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='dispatch_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.dispatch_detail'),
        ),
        migrations.AlterField(
            model_name='sales_voucher_stock_item_allocation',
            name='party_detail_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.party_details'),
        ),
    ]