# Generated by Django 3.0.8 on 2020-07-31 04:53

import backend.model.TutorialRelatedModel
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_auto_20200708_0010'),
    ]

    operations = [
        migrations.CreateModel(
            name='Uploads',
            fields=[
                ('is_published', models.BooleanField(default=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='%Y/%m/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='enus',
            options={'verbose_name': 'EN-US translation'},
        ),
        migrations.AlterModelOptions(
            name='zhcn',
            options={'verbose_name': 'ZH-CN translation'},
        ),
        migrations.AlterField(
            model_name='user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
