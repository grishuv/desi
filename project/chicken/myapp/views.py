# myapp/views.py
from django.shortcuts import render
from .models import Item

def item_list(request):
    items = Item.objects.all()
    return render(request, 'myapp/index.html', {'items': items})

def login(request):
    return render(request, 'myapp/login.html')