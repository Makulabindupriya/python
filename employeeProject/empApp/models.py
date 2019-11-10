from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField()
    ename=models.CharField(max_length=30)
    esal=models.FloatField()
    eaddr=models.CharField(max_length=100)
    def __str__(self): #when ever we are trying to print employee object internally we call this str method
        return self.ename
        return self.eno
#above method is the one type to display the object in admin interface
#py manage.py sqlmigrate empApp 0001 - to see the generated SQL Code
