from django.shortcuts import render
from django.http import HttpResponseRedirect
from prensa.forms import TensCis_Forms, MomFletor_Forms, MaxFlexao_Forms, TensNormal_Forms

def index(request):
    return render(request, 'index.html')

def cis(request):
    form = TensCis_Forms()
    contexto = {"form": form}
    return render(request, 'cis.html', contexto)

def fletor(request):
    form = MomFletor_Forms()
    contexto = {"form": form}
    return render(request, 'fletor.html', contexto)

def flex(request):
    form = MaxFlexao_Forms()
    contexto = {"form": form}
    return render(request, 'flex.html', contexto)

def normal(request):
    form = TensNormal_Forms()
    contexto = {"form": form}
    return render(request, 'normal.html', contexto)

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

def momFletor(request):
    if request.method == "POST":
        form = MomFletor_Forms(request.POST)
        if form.is_valid():
            contexto = {"form": form,
            "resultado": form.momFletor(),
            }  
            return render(request, "momFletor.html", contexto)
        else:
            print("form inválido")
            contexto = {"form": form}  
            return render(request, "fletor.html", contexto)   

def maxFlex(request):
    if request.method == "POST":
        form = MaxFlexao_Forms(request.POST)
        if form.is_valid():
            contexto = {"form": form,
            "resultado": form.maxFlexao(),
            }  
            return render(request, "maxFlex.html", contexto)
        else:
            print("form inválido")
            contexto = {"form": form}  
            return render(request, "flex.html", contexto) 

def tensNormal(request):
    if request.method == "POST":
        form = TensNormal_Forms(request.POST)
        if form.is_valid():
            contexto = {"form": form,
            "resultado": form.tensNormal(),
            }  
            return render(request, "tensNormal.html", contexto)
        else:
            print("form inválido")
            contexto = {"form": form}  
            return render(request, "normal.html", contexto) 
