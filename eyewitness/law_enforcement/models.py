from django.db import models
from django.contrib.auth.models import AbstractUser

class Photo(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(default="Aman")
    Height=models.FloatField(default=0.00)
    HairColor=models.TextField(default="Aman")
    HairType=models.TextField(default="Aman")
    EyeColor=models.TextField(default="Aman")
    Glasses=models.TextField(default="No")
    Scar=models.TextField(default="No")

    def __str__(self):
        return self.description

class Case(models.Model):
    class Meta:
        verbose_name = 'Case'
        verbose_name_plural = 'Cases'
    name = models.CharField(max_length=100, null=False, blank=False)
    photo_1 = models.ManyToManyField(Photo, blank=True, related_name="photo_1")
    photo_2 = models.ManyToManyField(Photo, blank=True, related_name="photo_2")
    photo_3 = models.ManyToManyField(Photo, blank=True, related_name="photo_3")
    

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_customer = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    case = models.ManyToManyField(Case, blank=True)

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)