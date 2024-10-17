from django.shortcuts import render
from .models import ToDoList
from .forms import CreateNewList
from django.http import HttpResponseRedirect

# Função que renderiza a página de uma lista específica
def index(response, id):
    # Obtém a lista de tarefas com o ID fornecido
    ls = ToDoList.objects.get(id=id)

    # Verifica se o método da requisição é POST
    if response.method == "POST":
        print(response.POST)  # Imprime os dados do POST para debug

        # Verifica se o botão "save" foi clicado
        if response.POST.get("save"):
            # Itera sobre todos os itens da lista
            for item in ls.item_set.all():
                # Marca o item como completo se o checkbox foi clicado
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                # Salva o estado do item
                item.save()

        # Verifica se o botão "newItem" foi clicado
        elif response.POST.get("newItem"):
            # Obtém o texto do novo item
            txt = response.POST.get("new")
            # Verifica se o texto tem mais de 2 caracteres
            if len(txt) > 2:
                # Cria um novo item na lista
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid")  # Imprime "Invalid" se o texto for muito curto

    # Renderiza a página da lista com o contexto da lista
    return render(response, "main/list.html", {"ls": ls})

# Função que renderiza a página inicial
def home(response):
    return render(response, "main/home.html", {})

# Função que cria uma nova lista
def create(response):
    # Verifica se o método da requisição é POST
    if response.method == "POST":
        # Cria um formulário com os dados do POST
        form = CreateNewList(response.POST)
        # Verifica se o formulário é válido
        if form.is_valid():
            # Obtém o nome da nova lista do formulário
            n = form.cleaned_data["name"]
            # Cria e salva a nova lista no banco de dados
            t = ToDoList(name=n)
            t.save()
            # Redireciona para a página da nova lista
            return HttpResponseRedirect("/%i" % t.id)
    else:
        # Cria um formulário vazio se o método não for POST
        form = CreateNewList()

    # Renderiza a página de criação de lista com o formulário
    return render(response, "main/create.html", {"form": form})