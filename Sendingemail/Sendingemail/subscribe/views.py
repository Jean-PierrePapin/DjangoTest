from django.shortcuts import render
from myproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = request.POST.get( 'subject', '' )
        message = request.POST.get( 'message', '' )
        recepient = request.POST.get( 'from email', '' )
        send_mail(subject, message, recepient, fail_silently = false)
        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'subscribe/index.html', {'form': sub})



