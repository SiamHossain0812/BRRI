from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name should be unique
    phone = models.CharField(max_length=15, unique=True)  # Phone number should be unique
    address = models.CharField(max_length=255)  # Address should be unique
    user_id = models.CharField(max_length=50, unique=True)  # User ID should be unique
    password = models.CharField(max_length=100)  # Password is typically not unique
    gateway_id = models.CharField(max_length=100, unique=True)  # Gateway ID should be unique

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user_info'


from django.db import models

class AdminInfo(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name should be unique
    phone = models.CharField(max_length=15, unique=True)  # Phone number should be unique
    address = models.CharField(max_length=255, unique=True)  # Address should be unique
    user_id = models.CharField(max_length=50, unique=True)  # User ID should be unique
    password = models.CharField(max_length=100)  # Password is typically not unique

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'admin_info'
