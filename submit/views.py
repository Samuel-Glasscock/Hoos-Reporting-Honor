from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm, ReportForm
from .models import Submission

def start_submission(request):
    if request.method == 'POST':
        form = StartSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return redirect('submit:report')
    else:
        form = StartSubmissionForm()
    return render(request, 'submit/start_submission.html', {'form': form})

def report(request):
    submission = get_object_or_404(Submission)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report updated successfully!')
            return redirect('submit:submission_complete')
    else:
        form = ReportForm(instance=submission)
    return render(request, 'submit/report.html', {'form': form, 'submission': submission})

def submission_complete(request):
    submission = get_object_or_404(Submission)
    return render(request, 'submit/submission_complete.html', {'submission': submission})

