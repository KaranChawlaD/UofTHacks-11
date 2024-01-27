from django.shortcuts import render, get_object_or_404
from .models import Memento
# Create your views here.

def index(request):
    mementos = Memento.objects.all()
    return render(request, 'index.html', {'mementos': mementos})

def memento(request, id):
    memento = get_object_or_404(Memento, id=id)
    return render(request, 'memento.html', {'memento': memento})

def addMemento(request):
    return render(request, 'add-memento.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'login.html')