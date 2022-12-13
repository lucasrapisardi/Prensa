from django.shortcuts import render
from django.http import HttpResponseRedirect
from prensa.forms import TensCis_Forms

def index(request):
    return render(request, 'index.html')

def cis(request):
    form = TensCis_Forms()
    contexto = {"form": form}
    return render(request, 'cis.html', contexto)

def fletor(request):
    return render(request, 'fletor.html')

def flex(request):
    return render(request, 'flex.html')

def normal(request):
    return render(request, 'normal.html')

def tensCis(request):
    if request.method == "POST":
        form = TensCis_Forms(request.POST)
        if form.is_valid():
            contexto = {"form": form,
            "resultado": form.tensaoCis(),
            }  
            return render(request, "tensCis.html", contexto)
        else:
            print("form inválido")
            contexto = {"form": form}  
            return render(request, "cis.html", contexto)   
