from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm 
from shared.forms import ReportForm, FileForm
from shared.models import Report, File

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
        form = ReportForm(request.POST)
        if form.is_valid():
            # Instead of saving the form, do something temporary with the data
            # For example, store it in the session
            request.session['report_data'] = form.cleaned_data
            messages.success(request, 'Report data temporarily stored.')
            return redirect('submit:submission_complete')
    else:
        form = ReportForm()
        # Optionally clear previous session data here to ensure a fresh start
        request.session.pop('report_data', None)
    return render(request, 'submit/report.html', {'form': form})

def submission_complete(request):
    # Retrieve data from the session and create a submission object
    # This step depends on how you intend to use the stored data
    report_data = request.session.pop('report_data', None)
    if report_data:
        # Process your report_data here, e.g., create a Submission object
        # submission = Submission.objects.create(**report_data)
        # Do something with the submission object
        pass
    else:
        # Handle cases where there is no data (e.g., direct access to this URL)
        messages.error(request, 'No report data found. Please start over.')
        return redirect('submit:report')

    return render(request, 'submit/submission_complete.html', {})


def report_submission(request):
    if request.method == 'POST':
        repoort_form = ReportForm(request.POST)
        file_form = FileForm(request.POST, request.FILES)
        if repoort_form.is_valid() and file_form.is_valid():
            new_report = repoort_form.save(commit=False)
            if request.user.is_authenticated:
                new_report.user = request.user
            else: 
                new_report.user = None
            new_report.save()

            if file_form.is_valid():
                files = request.FILES.getlist('file_field')
                for f in files:
                    File.objects.create(report=new_report, file=f)

            return redirect('submit:submission_complete')
        
    else:  
        report_form = ReportForm()
        file_form = FileForm()
    return render(request, 'submit/report_submission.html', {'report_form': report_form, 'file_form': file_form})

