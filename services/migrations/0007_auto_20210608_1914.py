# Generated by Django 3.2.3 on 2021-06-08 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_auto_20210608_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user_contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_msg',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_name',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='msg',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=100),
        ),
    ]
