from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm 
from shared.forms import ReportForm, FileForm
from shared.models import Report, File
from django.core.files.storage import default_storage

def start_submission(request):
    if request.method == 'POST':
        form = StartSubmissionForm(request.POST)
        if form.is_valid():
            # Instead of saving the form as a new Submission instance, store the data temporarily
            request.session['start_submission_data'] = form.cleaned_data
            messages.success(request, 'Start of submission temporarily stored.')
            return redirect('submit:report')
    else:
        form = StartSubmissionForm()
        # Optionally clear previous start submission data here to ensure a fresh start
        request.session.pop('start_submission_data', None)
    return render(request, 'submit/start_submission.html', {'form': form})

from django.contrib import messages

def report(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        file_form = FileForm(request.POST, request.FILES)
        if report_form.is_valid() and file_form.is_valid():
            new_report = report_form.save(commit=False)
            if request.user.is_authenticated:
                new_report.user = request.user
            new_report.save()

            # check if file was uploaded
            if file_form.is_valid():
                file = file_form.cleaned_data('file_field')
                if file:
                    File.objects.create(report=new_report, file=file)
            messages.success(request, 'You have successfully submitted your report.')
            return redirect('submit:submission_complete')
        else:
            messages.error(request, 'There was a problem with your submission.')
    else:
        report_form = ReportForm()
        file_form = FileForm()
    return render(request, 'submit/report.html', {'report_form': report_form, 'file_form': file_form})


def submission_complete(request):
    return render(request, 'submit/submission_complete.html', {})


# def report_submission(request):
#     if request.method == 'POST':
#         report_form = ReportForm(request.POST)
#         file_form = FileForm(request.POST, request.FILES)
#         if report_form.is_valid() and file_form.is_valid():
#             new_report = report_form.save(commit=False)
#             if request.user.is_authenticated:
#                 new_report.user = request.user
#             else: 
#                 new_report.user = None
#             new_report.save()

#             files = request.FILES.getlist('file_field')
#             for f in files:
#                 File.objects.create(report=new_report, file=f)

#             return redirect('submit:submission_complete')
        
#     else:  
#         report_form = ReportForm()
#         file_form = FileForm()
#     return render(request, 'submit/report_submission.html', {'report_form': report_form, 'file_form': file_form})

