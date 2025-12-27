# Ex01 Django ORM Web Application
# Date:18/11/2025
# AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

# ENTITY RELATIONSHIP DIAGRAM
## DESIGN STEPS
## STEP 1:
Clone the problem from GitHub

## STEP 2:
Create a new app in Django project

## STEP 3:
Enter the code for admin.py and models.py

## STEP 4:
Execute Django admin and create details for 6 cars

# PROGRAM
```
MODELS.PY

from django.db import models
from django.contrib import admin

class cars(models.Model):
    car_name=models.CharField(max_length=20)
    car_model=models.CharField(max_length=20)
    car_id=models.IntegerField()
    car_colour=models.CharField(max_length=20)

class carsAdmin(admin.ModelAdmin):
    list_display=['car_name','car_model','car_id','car_colour']

ADMIN.PY

from django.contrib import admin
from.models import cars,carsAdmin

admin.site.register(cars,carsAdmin)
   
```
# OUTPUT

![alt text](<Screenshot 2025-11-25 081321.png>)

# RESULT
Thus the program for creating a database using ORM hass been executed successfully
