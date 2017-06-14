from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/files/')

# Create your models here.
class STL(models.Model):
    stl_file = models.FileField(storage=fs)

class Gcode(models.Model):
    gcode_file = models.FileField(storage=fs)

class Filament(models.Model):
    #color =models.CharField(max_length=50)
    #inventory = models.IntegerField()
    #weight = models.IntegerField()
    #rolls_used = models.IntegerField()
    cost =  models.DecimalField(max_digits=4, decimal_places=2)
    markup = models.DecimalField(max_digits=2, decimal_places=2)
    # plastic type
    # Brand
    # Vendor

class Order(models.Model):
    stl = models.ForeignKey(STL, null=True)
    filament = models.ForeignKey(Filament, null=True)
    gcode = models.ForeignKey(Gcode, null=True)
    cost =  models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    grams = models.PositiveIntegerField(null=True)
    # payment status
    # date completed
    # client
    # class
    # filament
    # collection date



#class Student(models.Model):

#class Faculty(models.Model):

#class OL_staff(models.Model):

#class Course(models.Model):
