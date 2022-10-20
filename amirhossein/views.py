from multiprocessing import context
from django.shortcuts import render
from django.http import HttpRequest
from .models import Table

def table(request):
    query = Table.objects.all()
    context = {
        "data" : query , 
    }
    return render(request, 'table.html', context)

