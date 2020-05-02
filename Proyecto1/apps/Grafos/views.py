from django.shortcuts import render,redirect
from .forms import VerticeForm

def Home(request):
    return render(request,"index.html")


def CrearVertice(request):
    if request.method == "POST":
        vertice_form = VerticeForm(request.POST)
        if vertice_form.is_valid():
            vertice_form.save()
            return redirect("index")
    else:
        vertice_form = VerticeForm()
    return render(request,"grafo/crear_vertice.html",{"vertice_form":vertice_form})