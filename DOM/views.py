from django.shortcuts import render,HttpResponse
from DOM.models import Contacts
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def index(request):
    return render(request, 'index.html') 

def home(request):
    return HttpResponse("Hi this is home Page <h3>Hello My name is Aakash</h3>")

def about(request):
    return render(request, "about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        # contact=Contacts(name=name,email=email)
        # contact.save()
        subject="Welcome to Domestico Pvt Ltd."
        message=f'HI {name} , Thank you for registring'
        from_email=settings.EMAIL_HOST_USER
        recipient_list=[email,]
        send_mail(subject, message, from_email, recipient_list)
    return render(request, "contact.html")
    
def services(request):
    return render(request,"services.html")