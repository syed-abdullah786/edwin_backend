# Generated by Django 4.2.4 on 2023-09-09 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_templatedescription'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('streeteasy', 'streeteasy'), ('template', 'template'), ('costume', 'costume')], max_length=20),
        ),
    ]