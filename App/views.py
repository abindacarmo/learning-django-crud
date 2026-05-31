from django.shortcuts import render, redirect
from App.models import Estudante
from App.forms import EstudanteForm
from django.contrib import messages

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

def add_estudante(request):
    if request.method == "POST":
        form = EstudanteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "dados rai ho susesu!")
            return redirect("lista")
        
    return render(request, "add_estudante.html", {
        "form" : EstudanteForm()
    })

