# Generated by Django 5.1.4 on 2024-12-14 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_farmer_alter_saaoinformation_facebook_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PotentiometerData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField()),
                ('soil_moisture', models.FloatField()),
                ('water_level', models.FloatField()),
                ('require_water', models.FloatField()),
                ('rain', models.FloatField()),
                ('pump', models.BooleanField()),
                ('charge', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': '1123',
            },
        ),
    ]