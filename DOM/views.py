from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Home Page is showing like hot summer")

def home():
    return HttpResponse("Hi this is home Page <h3>Hello My name is Aakash</h3>")