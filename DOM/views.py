from django.shortcuts import render,HttpResponse
from DOM.models import Contacts

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
        contact=Contacts(name=name,email=email)
        contact.save()
    return render(request, "contact.html")
    
def services(request):
    return render(request,"services.html")