import random
import string
import uuid

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm 
from shared.forms import ReportForm, FileForm
from shared.models import Report, File
from django.core.files.storage import default_storage
from django.urls import reverse

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


def report(request):
    report_form = ReportForm(request.POST or None)
    file_form = FileForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if report_form.is_valid() and file_form.is_valid():
            new_report = report_form.save(commit=False)
            if request.user.is_authenticated:
                new_report.user = request.user

            # process data from student_involved field to ensure clean data by trimming and removing spaces
            students_involved_raw = report_form.cleaned_data['students_involved']
            student_involved_list = [student.strip() for student in students_involved_raw.split(',')]
            # if we want to process the list of students later, we can do so here such as accessing them to have their email later
            new_report.students_involved = ', '.join(student_involved_list)
            #Generating Case ID hash
            new_report.case_hash = uuid.uuid4()
            print(f"Generated Case ID hash at generation: {new_report.case_hash}")

            new_report.save()
            request.session['report_id'] = str(new_report.id)
            print(f"Generated Case ID hash at save: {new_report.case_hash}")

            # check if file was uploaded
            # if file_form.is_valid():
            file = file_form.cleaned_data.get('file_field')
            if file:
                File.objects.create(report=new_report, file=file)
            # messages.success(request, 'You have successfully submitted your report.')
            return redirect(reverse('submit:submission_complete'))
        
        # else:
        #     if not report_form.is_valid():
        #         messages.error(request, 'There was a problem with your report submission')
        #     if not file_form.is_valid():
        #         messages.error(request, 'There was a problem with your file submission')

    else:
        report_form = ReportForm()
        file_form = FileForm()
    return render(request, 'submit/report.html', {'report_form': report_form, 'file_form': file_form})


def submission_complete(request):
    report_id = request.session.get('report_id')
    # Access the report's ID from the session
    if not report_id:
        messages.error(request, "No recent submission found.")
        return redirect('shared:home')
    
    # Retrieve the report from the database using the ID
    try:
        report = Report.objects.get(id=report_id)
    except Report.DoesNotExist:
        messages.error(request, "Report not found.")
        return redirect('shared:home')
    
    case_hash = report.report_hash
    request.session.pop('report_id', None)
    context = {'case_hash': case_hash}

    return render(request, 'submit/submission_complete.html', context)


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

def incident_categories(request):
    return render(request, 'submit/incident_categories.html', {})
