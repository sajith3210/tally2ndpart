# Generated by Django 3.1.5 on 2023-04-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0019_auto_20230327_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='sales_invoice',
            name='party_ac_current_balance',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='party_ac_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='sales_ledger',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='sales_invoice',
            name='sales_ledger_ac_name',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sales_invoice',
            name='name_of_item',
            field=models.CharField(default='', max_length=200),
        ),
    ]
