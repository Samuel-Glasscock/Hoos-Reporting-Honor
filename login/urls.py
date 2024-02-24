from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('', views.home),
    path('logout/', views.logout_view),
]
