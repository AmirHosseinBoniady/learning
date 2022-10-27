from django.shortcuts import render
from .models import Car

def cars_detail(request):
    cars = Car.objects.all()
    return render(request, "cars detail.html", {'cars': cars})