

from django.contrib import admin
from django.urls import path
from App import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login_page, name="login_page"),
    path("home/", views.home, name="home"),
    path("konabaa/", views.konabaaa, name="kona-ba"),
    path("lista_estudante/", views.lista_estudante, name="lista"),
    path("aumenta_estudante/", views.add_estudante, name="input_estudante"),
    path("edit/<int:id>", views.edit_estudante, name='edit_estudante'),
    path("delete/<int:id>", views.delete_estudante, name='delete_estudante'),
    path("logout", views.logout_user, name="logout")
]
