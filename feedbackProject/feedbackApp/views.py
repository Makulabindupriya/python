from django.shortcuts import render
from . import forms

# Create your views here.
def thankyou_view(request):
    return render(request,'testApp/thankyou.html')

def feedback_view(request):
    if request.method=='GET': #we can also use this process but it is optional
        form=forms.FeedBackForm()
        #return render(request,'testApp/feedback.html',{'form':form}) #ignore this line if we are doing validations and use this at last of the code
    if request.method=='POST':
        form=forms.FeedBackForm(request.POST)#creating another form with the data coming from the request
        if form.is_valid():
            print('Form validation success and printing feedback info')
        #how we can capture the data from end-User.....for that we use 'cleaned_data' dictionary
            print('Student Name:',form.cleaned_data['name'])
            print('Student RollNo:',form.cleaned_data['rollno'])
            print('Student MailId:',form.cleaned_data['email'])
            print('Student Feedback:',form.cleaned_data['feedback'])
            return thankyou_view(request) #this will direct to thankyou.html page

        #the above code will be executed only when we submit the form
    return render(request,'testApp/feedback.html',{'form':form}) #we will not get empty form because the data code is executed first and again rendering the same data i.e..,control comes back to views

#GET -reading operation- just asking to get the requested data
#POST -update operation- to send the data to the server (here to get the data we have filled to the console (to display our data))

#How to send GET request: multiple ways are available
#1.   -open browser and enter url and Submit
#2.  -click the hyper links/anchor tags
#3.   -<form action='target'>
#       .....<form> - if method attribute is not there by default it is GET request
#4.   <form action='target' method='GET'>

#How to send POST request: one method is available
#   -to send POST request, form should be required and method should be explicitly declared as POST

#for more details go and search for "durga soft difference between get and post request". Two videos will be avialable for clear explanation.
