from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home Page is showing like hot summer")

def home(request):
    return HttpResponse("Hi this is home Page <h3>Hello My name is Aakash</h3>")

def about(request):
    return HttpResponse("Hi this is About page <h3>Hello My name is Aakash</h3>")

def contact(request):
    return HttpResponse("Hi this is contact page <h3>Hello My name is Aakash</h3>")
    
def services(request):
    return HttpResponse("Hi this is service Page <h3>Hello My name is Aakash</h3>")