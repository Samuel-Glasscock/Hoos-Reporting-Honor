from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm, ReportForm
from .models import Submission

def start_submission(request):
    if request.method == 'POST':
        form = StartSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save()
            return redirect('submit:report', submission_id=submission.id)
    else:
        form = StartSubmissionForm()
    return render(request, 'submit/start_submission.html', {'form': form})

def report(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            messages.success(request, 'Report updated successfully!')
            return redirect('submit:submission_complete', submission_id=submission.id)
    else:
        form = ReportForm(instance=submission)
    return render(request, 'submit/report.html', {'form': form, 'submission': submission})

def submission_complete(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    return render(request, 'submit/submission_complete.html', {'submission': submission})

