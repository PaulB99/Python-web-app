# Generated by Django 2.2.14 on 2020-08-25 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0003_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
    ]
