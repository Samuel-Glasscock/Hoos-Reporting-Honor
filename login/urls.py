from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('admin/', views.admin_home, name='admin_home'),
]
