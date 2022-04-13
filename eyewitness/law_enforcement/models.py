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
    

    def __str__(self):
        return self.name
        

class User(AbstractUser):
    is_officer = models.BooleanField(default=False)
    is_witness = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name


class Witness(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=20)
    case = models.ManyToManyField(Case, blank=True)
    def __str__(self):
        return self.user.first_name

class Officer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=20)
    designation = models.CharField(max_length=20)

class LineUp(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    photo = models.ForeignKey(Photo, blank=True, null=True, on_delete=models.SET_NULL)
    case =  models.ForeignKey(Case, blank=True, null=True, on_delete=models.SET_NULL)

class finalPhoto(models.Model):
    ide_photo = models.ForeignKey(LineUp, blank=True, null=True, on_delete=models.SET_NULL)
    confidence = models.IntegerField()