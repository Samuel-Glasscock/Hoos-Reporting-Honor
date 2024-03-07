from django.urls import path
from . import views

app_name = "submit"
urlpatterns = [
    path("", views.start_submission, name="start_submission"),
    path('<int:submission_id>/background/', views.background_info, name='background_info'),
    path('<int:submission_id>/involved_students', views.involved_students, name='involved_students'),
    path('<int:submission_id>/submission_complete', views.submission_complete, name='submission_complete')
]