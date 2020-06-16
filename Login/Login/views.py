from django.shortcuts import render

def home(request):
    return render(request, 'login.html')

def info(request):
    return render(request, 'infoPage.html')