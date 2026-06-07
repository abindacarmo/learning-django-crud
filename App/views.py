from django.shortcuts import render, redirect, get_object_or_404
from App.models import Estudante
from App.forms import EstudanteForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login_page")
def home(request):
    return render(request, "home.html")

@login_required(login_url="login_page")
def konabaaa(request):
    return render(request, "konaba.html")

@login_required(login_url="login_page")
def lista_estudante(request):
    estudante = Estudante.objects.all()
    context = {
        "estudantes" : estudante
    }
    return render(request, "lista_estudante.html", context)

@login_required(login_url="login_page")
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

@login_required(login_url="login_page")
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


@login_required(login_url="login_page")
def delete_estudante(request, id):
    estudante = get_object_or_404(Estudante, id=id)
    estudante.delete()
    return redirect("lista")

def login_page(request):
    form = UserLoginForm()
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Username ka Password Laloos!!")
    return render(request, "login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("login_page")


