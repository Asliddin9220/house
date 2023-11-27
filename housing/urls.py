from django.urls import path
from .views import main,contact,pd,properties

urlpatterns = [
    path('',main),
    path('contact.html/',contact),
    path('properties.html/',properties),
    path('property-details.html/',pd),
]