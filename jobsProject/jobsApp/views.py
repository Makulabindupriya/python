from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hydjobsinfo(request):
    s='Hyderabad Jobs Information'
    return HttpResponse(s)

def bnglrjobsinfo(request):
    s='<h1>Bangalore Jobs Information<h1>'
    return HttpResponse(s)

def chenjobsinfo(request):
    s='<h1>Chennai Jobs Information<h1>'
    return HttpResponse(s)
