from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = [
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    ]
    firstName = models.CharField(max_length=40)
    middleName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default="male")
    dateBirth = models.DateField()
    contactNumber = PhoneNumberField(region="PH")
    email = models.EmailField(max_length=200)
    Religion = models.CharField(max_length=200,default="christian")
    Barangay = models.CharField(max_length=200, default="fairview")
    City = models.CharField(max_length=200, default="quezon city")
    HouseNumber= models.IntegerField(default=0)
    Country = models.CharField(max_length=200, default="philippines")
    Zip = models.IntegerField(default=0)
    TIN = models.IntegerField(default=0)
    EmployeeStatus = models.CharField(max_length=200, default="active")
    Department = models.CharField(max_length=200, default="IT")
    Job = models.CharField(max_length=200, default="IT")
    # Manager

    def __str__(self):
        return self.firstName

class Department(models.Model):  
    
    name = models.CharField(max_length=100)  
    description = models.CharField(max_length=15)

    def __str__(self):
        return "%s " %(self.name) 
    class Meta:  
        db_table = "department"  