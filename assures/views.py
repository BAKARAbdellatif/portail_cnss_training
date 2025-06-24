from django.shortcuts import render, redirect

from assures.models import Assure
from assures.forms import FormAssure


# Create your views here.
def home(request):
    return render(request, 'home.html')


def index(request):
    assures = Assure.objects.all()
    return render(request, "assures/index.html", {'assures': assures})


def ajout(request):
    if request.method == "POST":
        form = FormAssure(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liste_assures")
    else:
        form = FormAssure()
    return render(request, "assures/ajout.html", {"form": form})


def edit(request, id):
    assure = Assure.objects.get(id=id)
    if request.method == "POST":
        form = FormAssure(request.POST, instance=assure)
        if form.is_valid():
            form.save()
            return redirect("liste_assures")
    else:
        form = FormAssure(instance=assure)
    return render(request, "assures/edit.html", {"form": form})


def delete(request, id):
    assure = Assure.objects.get(id=id)
    assure.delete()
    return redirect("liste_assures")

