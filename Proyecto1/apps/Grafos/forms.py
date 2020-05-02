from django import forms
from .models import Vertice

class VerticeForm(forms.ModelForm):
    class Meta:
        model = Vertice
        fields = ["nombre"]
        