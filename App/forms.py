from django import forms
from App.models import Estudante

class EstudanteForm(forms.ModelForm):
    class Meta:
        model = Estudante
        fields = "__all__"

        widgets = {
            "nre": forms.TextInput(attrs={"class": "form-control"}),
            "naran_aluno": forms.TextInput(attrs={"class": "form-control"}),
            "sexu": forms.Select(attrs={"class": "form-control"}),
            "idade": forms.NumberInput(attrs={"class": "form-control"}),
            "data_moris": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "hela_fatin": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "naran_dep": forms.Select(attrs={"class": "form-control"}),
            "status": forms.CheckboxInput(attrs={"class": "form-check-input"})

        }