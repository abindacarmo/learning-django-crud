

from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", views.home, name="home"),
    path("konabaa/", views.konabaaa, name="kona-ba"),
    path("lista_estudante/", views.lista_estudante, name="lista"),
    path("aumenta_estudante", views.add_estudante, name="input_estudante")
]
