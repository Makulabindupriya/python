from django.contrib import admin
from empApp.models import Employee

class EmployeeAdmin(admin.ModelAdmin): #this class method in admin.py is second method to dispolay all the details of the tables at a time in admin interface
    list_display=['eno','ename','esal','eaddr'] # we can add 'id' in display list optionally
# Register your models here.
admin.site.register(Employee,EmployeeAdmin) # this is just to register the model class in admin interface
