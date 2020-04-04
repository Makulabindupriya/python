from django import forms
from django.core import validators

def starts_with_d(value):
    if value[0]!='d': #if we are passing first letter as 'D' then use if value[0].lower()!='d':
        raise forms.ValidationError("Name should starts with d")

#we are passing validation that name should start with 'd' and even we can write seperate file for validators but whereever it is present should be available to forms.py file.

#   if value.isalpha!=True: ==>this is to validate whether the value passed is alphabets or not

def gmail_verification(mail):
    if mail[len(mail)-9:]!='gmail.com':
        raise forms.ValidationError('Must be gmail')

class FeedBackForm(forms.Form):
    name=forms.CharField(validators=[starts_with_d])
    rollno=forms.IntegerField() #max length is optional
    email=forms.EmailField(validators=[gmail_verification])


    password=forms.CharField(widget=forms.PasswordInput)
    repassword=forms.CharField(label='Password(Again)',widget=forms.PasswordInput) #we can define our own labels for display
    feedback=forms.CharField(widget=forms.Textarea,validators=[validators.MaxLengthValidator(40),validators.MinLengthValidator(10)])
    bot_handler=forms.CharField(required=False,widget=forms.HiddenInput) #to prevent malpractice from robotic script we are using this hidden field.This will not visible to end user,if we are geeting response from hidden field as well then we can come to know that is is not coming from human.this is coming form bot(robot script)
#the above attribute "validators" is implementing the implicit validators.if we want only one validators for above, just use only validators=[validators.MaxLengthValidator(40)]
#the sub-topic of forms is 'validations': validations are of two types:
#   -explicit validations implemented by programmers by using 'clean-methods'
#   -implicit validations provided by Django validators
#let us implement explicit form validations
    def clean_name(self): #this is fixed syntax, if we do any mistakes then Django will not call this method
      inputname=self.cleaned_data['name']
      print('validating name')
      if len(inputname)<4:
          raise forms.ValidationError('The length of name field should be greater than or equal to 4')
      return inputname # this will return the name value only if the validation is valid.
    def clean_rollno(self):
      inputrollno=self.cleaned_data['rollno']
      print('validationg rollno')
      return inputrollno

    def clean_email(self):
      inputemail=self.cleaned_data['email']
      print('validationg email')
      return inputemail

    def clean_feedback(self):
      inputfeedback=self.cleaned_data['feedback']
      print('validationg feedback')
      return inputfeedback #please check and implement explicit seperate validations for pasword and repassword as well



#let us know about implicit validators
#to implement implicit validators we have to import validators from django.core module


#instead of implementing the explict validations seperately...we can also declare all validation in single Function
    def clean(self):
          print('Total Form Validation and Bot validation....')
          cleaned_data=super().clean() #clean() method is from 'forms.Form' class(parent class of FeedBackForm) 
          bot_handler_value=cleaned_data['bot_handler'] #cleaned data provided whatever data provided by end-user
          if len(bot_handler_value)>0:
              raise forms.ValidationError('Thanks Bot!!!')
          inputname=cleaned_data['name']
          if len(inputname) < 10:
              raise forms.ValidationError('Name should contain minimum 10 characters')
          inputrollno=cleaned_data['rollno']
          if len(str(inputrollno)) != 3:
              raise forms.ValidationError('Rollno should compulsory contains exactly 3 digits')
          inputpwd=cleaned_data['password']
          inputrepwd=cleaned_data['repassword']
          if inputpwd != inputrepwd:
              raise forms.ValidationError('Passwords not matched')
