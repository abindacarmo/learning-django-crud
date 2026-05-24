from django.shortcuts import render
from App.models import Estudante

# Create your views here.

def home(request):
    return render(request, "home.html")

def konabaaa(request):
    return render(request, "konaba.html")


def lista_estudante(request):
    estudante = Estudante.objects.all()
    context = {
        "estudantes" : estudante
    }
    return render(request, "lista_estudante.html", context)