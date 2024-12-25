# Generated by Django 5.1.4 on 2024-12-14 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_alter_admininformation_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='UAOInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('upazila', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('aez', models.CharField(max_length=100)),
                ('hotspot', models.CharField(max_length=100)),
                ('risk_area', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=50)),
                ('personal_phone', models.CharField(max_length=15)),
                ('official_phone', models.CharField(max_length=15)),
                ('whatsapp_number', models.CharField(max_length=15)),
                ('facebook_id', models.CharField(max_length=100)),
                ('official_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'UAOInformation',
            },
        ),
    ]