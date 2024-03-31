from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponse
from .models import Report, File
import boto3
from urllib.parse import urlparse


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if hasattr(request.user, "profile") and request.user.profile.is_admin:
        # call shared:view_files
            return redirect('shared:admin_report_list')
        else: # home page for logged in user?
            return render(request, "shared/home.html")
    else: # home page for anonymous user?
        return render(request, "shared/home.html")  

def is_site_admin(user):
    return user.is_authenticated and (user.is_staff or user.profile.is_admin)

@login_required
@user_passes_test(is_site_admin)
def admin_report_list(request):
    completed_reports = Report.objects.prefetch_related('file_set').all()
    return render(request, 'shared/admin_home.html', {'reports': completed_reports})

@login_required
@user_passes_test(is_site_admin)
# @permission_required('shared.view_report', raise_exception=True)
def report_detail(request, report_id):
    report = get_object_or_404(Report.objects.prefetch_related('file_set'), pk=report_id)
    return render(request, 'shared/report_details.html', {'report': report})

def upload_test(request):
    if request.method == 'POST':
        # get report 0 to test
        report = Report.objects.get(pk=0)
        for file in request.FILES.getlist('file'):
            File.objects.create(report=report, file=file)
        return redirect('404.html')
    return render(request, 'shared/upload_test.html')

def view_files(request):
    # get all file objects from s3
    files = File.objects.all()
    return render(request, 'shared/view_files.html', {'files': files})

def render_object_from_s3(request, s3_object_url):
    s3 = boto3.client('s3')
    parsed_url = urlparse(s3_object_url)
    bucket_name = 'honor-code-reporting-a-22'
    object_key = parsed_url.path.lstrip('/')
    file = s3.get_object(Bucket=bucket_name, Key=object_key)
    object_data = file['Body'].read()
    content_type = file['ContentType']
    response = HttpResponse(object_data, content_type=content_type)
    return response
