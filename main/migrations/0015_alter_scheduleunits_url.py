# Generated by Django 4.2.4 on 2023-12-26 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_scheduleunits'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduleunits',
            name='url',
            field=models.URLField(),
        ),
    ]
