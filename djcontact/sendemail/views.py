# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.conf import settings

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            settings.EMAIL_HOST_PASSWORD='raionzo@25'
            settings.EMAIL_HOST_USER = 'raionzouser@gmail.com'
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['from_email']
            var_email = form.cleaned_data['from_email']
            mobile_no = form.cleaned_data['mobile_no']
            messages = form.cleaned_data['messages']
            try:
                send_mail(from_email, "Name :" +  name + " " + "Mobile :" + mobile_no + " "+ "Message :" + messages, var_email, ['raionzoiarc@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')
