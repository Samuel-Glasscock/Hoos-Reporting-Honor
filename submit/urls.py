from django.urls import path
from . import views
from .views import anonymous_submission

app_name = "submit"
urlpatterns = [
    path("anonymous_submission/", anonymous_submission, name="anonymous_submission"),
]