# manage your viwes here
from . import views
from django.urls import path

# URL routing patterns for navigating

urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name=""),
    path("about",views.about,name=""),
    path("contact",views.contact,name=""),
    path("services",views.services,name=""),
]