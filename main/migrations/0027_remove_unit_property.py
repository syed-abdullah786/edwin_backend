# Generated by Django 4.2.4 on 2024-05-08 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_alter_unit_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='property',
        ),
    ]