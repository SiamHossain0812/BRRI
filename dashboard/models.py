from django.db import models


class AdminInformation(models.Model):
    # Personal Information
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    age = models.PositiveIntegerField()

    # Location & Division Details
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    division = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    upazila = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    aez = models.CharField(max_length=255)
    hotspot = models.CharField(max_length=255)
    risk_area = models.CharField(max_length=255)

    # Contact Information & Miscellaneous
    nid = models.CharField(max_length=20)
    personal_phone = models.CharField(max_length=20)
    official_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    facebook_id = models.CharField(max_length=255)
    official_email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'AdminInformation'
        
        
from django.db import models

class UAOInformation(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    
    latitude = models.FloatField()
    longitude = models.FloatField()
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    aez = models.CharField(max_length=100)
    hotspot = models.CharField(max_length=100)
    risk_area = models.CharField(max_length=100)

    nid = models.CharField(max_length=50)
    personal_phone = models.CharField(max_length=15)
    official_phone = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)
    facebook_id = models.CharField(max_length=100)
    official_email = models.EmailField()

    def __str__(self):
        return f"{self.name} - {self.father_name}"
    
    class Meta:
        db_table = 'UAOInformation'

from django.db import models

from django.db import models

class SAAOInformation(models.Model):
    name = models.CharField(max_length=255)
    father_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    age = models.IntegerField()
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    union = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    aez = models.CharField(max_length=100)
    hotspot = models.CharField(max_length=100)
    risk_area = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    nid = models.CharField(max_length=20)
    personal_phone = models.CharField(max_length=20)
    official_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    facebook_id = models.CharField(max_length=255)
    official_email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'SAAOInformation'


from django.db import models

# Farmer Registration Model
class Farmer(models.Model):
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    gwid = models.CharField(max_length=50, unique=True)  # Device ID (GWID)
    latitude = models.FloatField()
    longitude = models.FloatField()
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    upazila = models.CharField(max_length=100)
    union = models.CharField(max_length=100)
    block = models.CharField(max_length=100)
    villaige = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    aez = models.CharField(max_length=100)
    hotspot = models.CharField(max_length=100)
    risk_area = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    nid = models.CharField(max_length=100)
    agril = models.CharField(max_length=100)  # Agricultural Smart Card Number
    personal_phone = models.CharField(max_length=20)
    secondary_phone = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    imo_number = models.CharField(max_length=20)
    facebook_id = models.CharField(max_length=100)
    official_email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'FarmerInformation'
        

from django.db import models

class PotentiometerData(models.Model):
    temperature = models.FloatField()
    soil_moisture = models.FloatField()
    water_level = models.FloatField()
    require_water = models.FloatField()
    rain = models.FloatField()
    pump = models.BooleanField()
    charge = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '1123'  # Set the table name here
        
class LaserData(models.Model):
    temperature = models.FloatField()
    soil_moisture = models.FloatField()
    water_level = models.FloatField()
    require_water = models.FloatField()
    rain = models.FloatField()
    pump = models.BooleanField()
    charge = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '1124'  # Set the table name here
        
class UltraSoundData(models.Model):
    temperature = models.FloatField()
    soil_moisture = models.FloatField()
    water_level = models.FloatField()
    require_water = models.FloatField()
    rain = models.FloatField()
    pump = models.BooleanField()
    charge = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = '1125'  # Set the table name here        

