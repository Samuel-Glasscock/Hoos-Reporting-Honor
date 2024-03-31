from django.urls import path
from . import views

app_name = "shared"
urlpatterns = [
    path("", views.home, name="home"),
    path("reports/admin", views.admin_report_list, name="admin_report_list"),
    path("upload_test", views.upload_test, name="upload_test"),
    path("view_files", views.view_files, name="view_files"),
    path("render_object_from_s3/<path:s3_object_url>", views.render_object_from_s3, name="render_object_from_s3"),
    path("render_object_from_s3/<path:s3_object_url>", views.render_object_from_s3, name="render_object_from_s3"),
    path('report/<int:report_id>', views.report_detail, name='report_detail'),
]
