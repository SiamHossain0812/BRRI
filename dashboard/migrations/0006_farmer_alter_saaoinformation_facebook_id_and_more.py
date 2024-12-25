# Generated by Django 5.1.4 on 2024-12-14 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_saaoinformation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('father_name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('gwid', models.CharField(max_length=50, unique=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('upazila', models.CharField(max_length=100)),
                ('union', models.CharField(max_length=100)),
                ('block', models.CharField(max_length=100)),
                ('villaige', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('aez', models.CharField(max_length=100)),
                ('hotspot', models.CharField(max_length=100)),
                ('risk_area', models.CharField(max_length=100)),
                ('education', models.CharField(max_length=100)),
                ('nid', models.CharField(max_length=100)),
                ('agril', models.CharField(max_length=100)),
                ('personal_phone', models.CharField(max_length=20)),
                ('secondary_phone', models.CharField(max_length=20)),
                ('whatsapp_number', models.CharField(max_length=20)),
                ('imo_number', models.CharField(max_length=20)),
                ('facebook_id', models.CharField(max_length=100)),
                ('official_email', models.EmailField(max_length=254)),
            ],
            options={
                'db_table': 'FarmerInformation',
            },
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='facebook_id',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='gender',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='nid',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='official_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='personal_phone',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='saaoinformation',
            name='whatsapp_number',
            field=models.CharField(max_length=20),
        ),
    ]