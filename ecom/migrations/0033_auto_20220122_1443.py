# Generated by Django 2.2.26 on 2022-01-22 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0032_auto_20220122_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(to='ecom.Cart'),
        ),
    ]