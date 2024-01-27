from django.shortcuts import render, get_object_or_404
from .models import Memento
# Create your views here.

def index(request):
    mementos = Memento.objects.all()
    return render(request, 'index.html', {'mementos': mementos})

def memento(request, id):
    memento_id = get_object_or_404(Memento, id=id)
    mementos = Memento.objects.all()

    context = {
        'memento_id': memento_id,
        'mementos': mementos
    }

    return render(request, 'mementos.html', context)

def addMemento(request):
    return render(request, 'add-memento.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'login.html')