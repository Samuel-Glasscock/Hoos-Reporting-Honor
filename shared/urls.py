from django.urls import path
from . import views

app_name = "shared"
urlpatterns = [
    path("", views.home, name="home"),
    path("admin/reports", views.admin_report_list, name="admin_report_list"),
]
