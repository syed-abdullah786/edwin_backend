# Generated by Django 4.2.4 on 2024-05-09 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_jobpropertybridge'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpropertybridge',
            name='property_url',
            field=models.URLField(default=''),
        ),
    ]
