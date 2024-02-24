from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path('', views.home),
    path('logout/', views.logout_view),
    path("", views.login_view, name="login_view"),
    path("login_request/", views.login_request, name="login_request"),
]
