# Generated by Django 2.2.14 on 2020-08-24 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualification',
            name='text',
            field=models.TextField(default=''),
        ),
    ]