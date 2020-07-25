from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def sendingemails(request):
    return render(request, 'sendingemails.html')