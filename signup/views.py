from django.shortcuts import render
from django.http import HttpResponse


def webpage_one(request):
    return render(request,'landing.html')


def webpage_two(request):
    return render(request,'signup.html')


def webpage_three(request):
    return render(request,'signupdone.html')
