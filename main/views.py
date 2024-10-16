from django.shortcuts import render
from .models import ToDoList
from .forms import CreateNewList
from django.http import HttpResponseRedirect


# Create your views here.
def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, "main/list.html", {"ls": ls})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)  # passa um dict com dados digitados no form
        if form.is_valid():  # se for valido salva os dados no banco
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
        return HttpResponseRedirect(
            "/%i" % t.id
        )  # redireciona para a pagina do novo item
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})
