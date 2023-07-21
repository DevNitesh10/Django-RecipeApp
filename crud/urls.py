from django.urls import path
from .views import index, about, create, contacts, partData

urlpatterns = [
    path("",index, name="home"),
    path("about-us/",about, name="about"),
    path("create/", create, name="create"),
    path("contacts/", contacts, name="contacts"),
    path("<id>/", partData, name="partData")
]
