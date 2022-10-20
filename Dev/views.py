from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    qs = Book.objects.all()
    context = {
        'qs': qs
    }
    return render(request, 'book.html', context)