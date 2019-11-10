from django.shortcuts import render
from django.http import HttpResponse
from empApp.models import Employee

# Create your views here.
def index(request):
    return render(request,'testApp/index.html')
def empview(request):
    emp_list=Employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testApp/emp.html',context=my_dict)
