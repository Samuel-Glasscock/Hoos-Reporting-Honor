from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Report, File

# Create your views here.
def home(request):
    if request.user.profile.is_admin:
        return render(request, "login/admin_home.html")
    elif request.user.is_authenticated:
        return render(request, "submit/start_submission.html")
    return render(request, "404.html")

def is_site_admin(user):
    return user.is_authenticated and (user.is_staff or user.profile.is_admin)

@login_required
@user_passes_test(is_site_admin)
def admin_report_list(request):
    completed_reports = completed_reports.prefetch_related('file_set')
    return render(request, 'reports/admin_report_list.html', {'reports': completed_reports})

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