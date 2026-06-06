from django.shortcuts import render, redirect, get_object_or_404
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

def edit_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    if request.method == 'POST':
        form = EstudanteForm(request.POST, instance=estudante)
        if form.is_valid():
            form.save()
            return redirect("lista")
    
    return render(request, "edit_estudante.html", {
        "form" : EstudanteForm(instance=estudante)
    })


def delete_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect("lista")