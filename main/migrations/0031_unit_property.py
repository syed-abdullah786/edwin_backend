# Generated by Django 4.2.4 on 2024-05-10 11:45

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0030_jobpropertybridge_property_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.property'),
            preserve_default=False,
        ),
    ]
