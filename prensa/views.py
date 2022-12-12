from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def cis(request):
    return render(request, 'cis.html')

def fletor(request):
    return render(request, 'fletor.html')

def flex(request):
    return render(request, 'flex.html')

def normal(request):
    return render(request, 'normal.html')
