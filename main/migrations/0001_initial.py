# Generated by Django 4.2.4 on 2023-09-03 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urls', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('scraped', 'scraped')], max_length=20)),
                ('isProcessing', models.IntegerField(default=0)),
                ('neighbour', models.JSONField(default={'Bronx': [], 'Brooklyn': [], 'Manhattan': [], 'Others': [], 'Queens': [], 'Staten_Island': []})),
                ('upload_img', models.BooleanField(default=False)),
                ('images', models.JSONField(default={'bathroom': {'furnished': [], 'unfurnished': []}, 'bedroom': {'furnished': [], 'unfurnished': []}, 'golf_room': {'furnished': [], 'unfurnished': []}, 'gym': {'furnished': [], 'unfurnished': []}, 'kitchen': {'furnished': [], 'unfurnished': []}, 'livingroom': {'furnished': [], 'unfurnished': []}, 'lobby': {'furnished': [], 'unfurnished': []}, 'lounge': {'furnished': [], 'unfurnished': []}, 'others': {'furnished': [], 'unfurnished': []}, 'pool': {'furnished': [], 'unfurnished': []}, 'roof_deck': {'furnished': [], 'unfurnished': []}})),
            ],
        ),
        migrations.CreateModel(
            name='RealityUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('unit', models.CharField(max_length=10, null=True)),
                ('complete_title', models.CharField(max_length=150, null=True)),
                ('beds', models.CharField(max_length=20)),
                ('baths', models.CharField(max_length=15)),
                ('price', models.CharField(max_length=10)),
                ('listing_id', models.IntegerField(default=None, null=True)),
                ('image_urls', models.TextField(null=True)),
                ('image_paths', models.JSONField(null=True)),
                ('description', models.TextField(null=True)),
                ('amenities', models.JSONField(null=True)),
                ('added_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('scraped', 'scraped')], max_length=20)),
                ('isProcessing', models.IntegerField(default=0)),
                ('convertible', models.IntegerField(default=0)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.property')),
                ('reality_user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.realityuser')),
            ],
        ),
    ]
