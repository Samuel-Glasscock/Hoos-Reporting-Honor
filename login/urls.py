from django.urls import path
from . import views

app_name = "login"
urlpatterns = [
    path("", views.login_view, name="login_view"),
    path("login_request/", views.login_request, name="login_request"),
    path('admin/', views.admin_home, name='admin_home'),
    path('google_login_request/', views.google_login_request, name='google_login_request'),
]
