# Generated by Django 3.0.8 on 2020-07-08 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_auto_20200706_0411'),
    ]

    operations = [
        migrations.AddField(
            model_name='graph',
            name='categories',
            field=models.ManyToManyField(default='uncategorized', to='backend.Category'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='categories',
            field=models.ManyToManyField(default='uncategorized', to='backend.Category'),
        ),
    ]
