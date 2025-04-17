from django.db import models
from rest_framework import serializers
from django.core.validators import MaxValueValidator,MinValueValidator
from django.contrib.auth.models import User



class ShowroomModel(models.Model):
    name=models.CharField(max_length=30)
    location=models.CharField(max_length=100)
    webside=models.URLField(max_length=100)

    def __str__(self):
        return self.name

# def isAlphanumeric(value):
#     if value not in value


class CarModel(models.Model):
    model_no=models.CharField(max_length=4)
    name=models.CharField(max_length=20)
    descripe=models.TextField(max_length=50)
    price = models.DecimalField(max_digits=8,decimal_places=2,null=True,blank=True)
    showroom=models.ForeignKey(ShowroomModel,on_delete=models.CASCADE,null=True,related_name="showrooms")
    create_at=models.DateTimeField(auto_now_add=True)
    updated_to=models.DateTimeField(auto_now=True)

    def __str__(self):
        #return f"{self.name} - {self.model_no}"
        return self.name
    

class ReviewModel(models.Model):
    userapi=models.ForeignKey(User,on_delete=models.CASCADE)
    star=models.IntegerField(validators=[MaxValueValidator,MinValueValidator])
    comments=models.CharField(max_length=100)
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name="reviews")


    def __str__(self):
        return self.comments

