# Generated by Django 4.1.6 on 2023-02-02 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_address_zip_code'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customer',
            table='store_customers',
        ),
    ]
