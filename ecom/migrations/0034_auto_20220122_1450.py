# Generated by Django 2.2.26 on 2022-01-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0033_auto_20220122_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ManyToManyField(to='ecom.Cart'),
        ),
    ]
