from django.urls import path
from . import views

app_name = "history"
urlpatterns = [
# path("case/<int:id>/", views.case, name="case"),
path("lookup/", views.lookup, name="lookup"),
path("dashboard/", views.dashboard, name="dashboard"),
# path("dashboard/<int:id>", views.report, name="report"), # possibly delete for security?
path("delete/", views.delete, name="delete"),
path("report-details/", views.report_details, name="report_details"),
]