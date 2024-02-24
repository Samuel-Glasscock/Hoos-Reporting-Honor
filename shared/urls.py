from django.urls import path
from . import views

app_name = "shared"
urlpatterns = [
    path("", views.home, name="home")
    
]
