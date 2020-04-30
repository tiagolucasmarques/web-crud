from django.shortcuts import render, redirect  
from .models import Produto  
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
 
def home(request):
    return render(request, 'home.html')

def list_items(request):
    data = {}
    data['list'] = []
    data['error'] = []
    try:
        data['list'] = Produto.objects.all()
    except:
         data['error'].append("Erro ao carregar o  Produto !!! ")
    return render(request, 'items.html', data)

@csrf_exempt
def new_items(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'POST':
        id = int(request.POST.get('id', -1))
        name = request.POST.get('name')
        quantidade = request.POST.get('quantidade')
        valor = request.POST.get('valor')
        try:
            if (id == -1):
                items = Produto(name=name, quantidade=quantidade, valor=valor)
                items.save()
            else:
                items = Produto.objects.get(id=id)
                items.name = name
                items.quantidade = quantidade
                items.valor = valor
                items.save()
        except:
            data['error'].append("Erro ao cadastrar Produto no banco !!! ")
            return render(request, 'items.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar Produto no banco !!! ")
            return render(request, 'items.html', data)
        return render(request, 'items.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro !! Tente Novamente mais tarde !! ")
        return render(request, 'items.html', data)

def delete_items(request):
    data = {}
    data['list'] = []
    data['error'] = []
    if request.method == 'GET':
        id = int(request.GET.get('id'))
        try:
            items = Produto.objects.get(id=id)
            items.delete()
        except:
            data['error'].append("Erro ao deletar Produto !!! ")
            return render(request, 'items.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar Produto !!! ")
            return render(request, 'items.html', data)
        return render(request, 'items.html', data)
    else:
        data['error'].append("Erro no sistema de cadastro  !!! Tente  Novamente mais tarde! ")
        return render(request, 'items.html', data)

def update_items(request):
    data = {}
    data['list'] = []
    data['error'] = []
    data['items'] = []
    if request.method == 'GET':
        id = request.GET.get('id')
        try:
            data['items'].append(Produto.objects.get(id=id))
        except:
            data['error'].append("Erro ao carregar Produto  !!! ")
            return render(request, 'items.html', data)
        try:
            data['list'] = Produto.objects.all()
        except:
            data['error'].append("Erro ao carregar Produto !!! ")
            return render(request, 'items.html', data)
        return render(request, 'items.html', data)
    else:
        data['Error'].append("Erro no sistema de cadastro! Tente Novamente mais tarde !!! ")
        return render(request, 'items.html', data)
    
