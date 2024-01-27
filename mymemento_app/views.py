from django.shortcuts import render
from .models import Memento
# Create your views here.

def index(request):
    mementos = Memento.objects.all()
    return render(request, 'index.html', {'mementos': mementos})

def addMemento(request):
    return render(request, 'add-memento.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'login.html')