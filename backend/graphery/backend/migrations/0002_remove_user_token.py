# Generated by Django 3.0.7 on 2020-06-17 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='token',
        ),
    ]
