from django.db import models
from django.contrib import admin

class cars(models.Model):
    car_name=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    car_id=models.IntegerField()
    car_colour=models.CharField(max_length=20)

class carsAdmin(admin.ModelAdmin):
    list_display=['car_name','car_model','car_id','car_colour']
   



# Create your models here.
