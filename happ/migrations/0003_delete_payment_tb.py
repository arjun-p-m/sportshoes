# Generated by Django 4.0.6 on 2022-08-22 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('happ', '0002_remove_product_tb_admin'),
    ]

    operations = [
        migrations.DeleteModel(
            name='payment_tb',
        ),
    ]