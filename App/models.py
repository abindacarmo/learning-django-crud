from django.db import models

# Create your models here.

class Departamento(models.Model):
    id_dep = models.CharField(max_length=10, unique=True, blank=False)
    naran_dep = models.CharField(max_length=80, blank=False)

    def __str__(self):
        return self.naran_dep
        


class Estudante(models.Model):
    nre = models.CharField(max_length=11, unique=True, blank=False)
    naran_aluno = models.CharField(max_length=200, blank=False)
    sexu = models.CharField(max_length=4, choices=[
        ("Mane", "Mane"),
        ("Feto", "Feto"),
    ], default="Mane")
    idade = models.IntegerField()
    data_moris = models.DateField()
    hela_fatin = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=80)
    status = models.BooleanField(default=True)
    naran_dep = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.naran_aluno
