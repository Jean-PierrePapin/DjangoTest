from django.shortcuts import render
# from myproject.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail

import smtplib

from email.mime.text import MIMEText



def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        """ msg = MIMEText('Testing some Mailgun awesomness')
        msg['Subject'] = "Hello"
        msg['From']    = "foo@YOUR_DOMAIN_NAME"
        msg['To']      = "bar@example.com"

        s = smtplib.SMTP('smtp.mailgun.org', 587)

        s.login('postmaster@YOUR_DOMAIN_NAME', '3kh9umujora5')
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        s.quit() """


        sub = forms.Subscribe(request.POST)
        subject = request.POST.get( 'subject', '' )
        message = request.POST.get( 'message', '' )
        recepient = request.POST.get( 'from email', '' )
        send_mail(subject, message, recepient, fail_silently = False)

        return render(request, 'subscribe/success.html', {'recepient': recepient})
    return render(request, 'sendingemails.html', {'form': sub})



