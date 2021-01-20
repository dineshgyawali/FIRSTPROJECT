from django.shortcuts import render
from .forms import AttendanceForm, Customer_form, Staff_form, Support_form

# Create your views here.

from django.http import HttpResponse


def Hello(request):
    return HttpResponse("Hello")

def World(request):
    return HttpResponse("World")

def welcome(request):
    context = {'tag_var':"tag_var"}
    return render(request,"app1.html",context)


def Attendanceview(request):
    form = AttendanceForm()
    context = {'form':form}
    return render(request,"app1.html",context)

def Submission(request):
    return HttpResponse("Thank you for your submission")

def Csview(request):
    form = Customer_form(request.POST or None)
    if form. is_valid():
        form.save()
        form = Customer_form()

    context = {'form':form}
    return render(request,"app1a.html",context)

def Staffview(request):
    form = Staff_form(request.POST or None)
    if form. is_valid():
        form.save()
        form = Staff_form()

    context = {'form':form}
    return render(request,"app1a.html",context)


def Supportview(request):
    form = Support_form(request.POST or None)
    if form. is_valid():
        form.save()
        form = Support_form()

    context = {'form':form}
    return render(request,"app1a.html",context)
