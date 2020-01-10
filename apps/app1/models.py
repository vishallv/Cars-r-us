from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class Lister(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    latitude = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    car_type = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    rental_price = models.FloatField()
    image = models.ImageField(upload_to='car_image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
class Dates(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    user = models.ForeignKey(User,related_name="dates")
    lister = models.ForeignKey(Lister,related_name="dates")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    