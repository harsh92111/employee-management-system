from django.db import models

# Create your models here.
class Position(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):                  #whenever position class will be called it will return title and not position object 
        return self.title

class Employee(models.Model):
    fullname=models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile=models.CharField(max_length=15)
    position=models.ForeignKey(Position,on_delete=models.CASCADE) #on deleting position employee table with that position
                                                                   #also get deleted
