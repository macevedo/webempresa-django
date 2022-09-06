from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name','')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos
            email = EmailMessage(
                "La Caffettiera: nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribrio:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["maximilian.acevedo@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
            except:
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form': contact_form})
