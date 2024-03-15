from django.urls import path
from . import views

app_name = "submit"
urlpatterns = [
    path("", views.start_submission, name="start_submission"),
    path("report/<int:submission_id>", views.report, name="report"),
    path("submission_complete/<int:submission_id>", views.submission_complete, name="submission_complete"),
]
