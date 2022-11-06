# manage your viwes here
from . import views
from django.urls import path

# URL routing patterns for navigating

urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("services",views.services,name="services"),
]