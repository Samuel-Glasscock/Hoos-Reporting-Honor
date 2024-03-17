from django.urls import path
from . import views
from .views import anonymous_submission

app_name = "submit"
urlpatterns = [
    path("", views.start_submission, name="start_submission"),
    path("report", views.report, name="report"),
    path("submission_complete", views.submission_complete, name="submission_complete"),
    path("anonymous_submission/", anonymous_submission, name="anonymous_submission"),
]
