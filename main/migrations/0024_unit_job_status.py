# Generated by Django 4.2.4 on 2024-05-06 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_property_urls_jobs_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='unit',
            name='job_status',
            field=models.CharField(default='resume', max_length=20),
        ),
    ]
