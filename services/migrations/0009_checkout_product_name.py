# Generated by Django 3.2.3 on 2021-06-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0008_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='Product_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]