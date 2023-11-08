from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname = models.CharField(max_length=50)
    Lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.CharField(max_length=50)
    Rollnumber = models.CharField(max_length=50)
    Semester = models.CharField(max_length=30)

    # Convert Object into a String
    def __str__(self):
        return self.Firstname
    
class Car(models.Model):
    CarName = models.CharField(max_length=50)
    Speed = models.IntegerField(max_length=50)
    
    def __str__(self) -> str:
        return self.CarName
    