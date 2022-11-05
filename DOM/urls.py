# manage your viwes here
from . import views
from django.urls import path

urlpatterns = [
    path("",views.index,name="index"),
    path("home",views.home,name=""),
    path("about",views.home,name=""),
    path("contact",views.home,name=""),
    path("services",views.home,name=""),
]