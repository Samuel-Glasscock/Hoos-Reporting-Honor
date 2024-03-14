from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import StartSubmissionForm, ReportForm
from .models import Submission


def start_submission(request):
    if request.method == 'POST':
        form = StartSubmissionForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            # You can add additional processing here
            submission.save()
            # Redirect to the next step, passing the submission ID
            return redirect('report', submission_id=submission.id)
    else:
        form = StartSubmissionForm()
    return render(request, 'submit/start_submission.html', {'form': form})


def report(request):
    submission = get_object_or_404(Submission)
    if request.method == 'POST':
        form = ReportForm(request.POST, instance=submission)
        if form.is_valid():
            form.save()
            # Redirect to the next part of the process or to a completion page
            return redirect('submission_complete')
    else:
        form = ReportForm(instance=submission)
    return render(request, 'submit/report.html', {'form': form})


def submission_complete(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)

    # 1 final validation checks or data processing before marking the submission as complete.
    # if not submission.is_valid():
    #     return redirect('previous_step_url', submission_id=submission.id)  # Redirect back if needed

    # 2 how to clear session data if we need to?
    # if 'submission_data' in request.session:
    #     del request.session['submission_data']

    # 3 mark as completed (need to set up a field for that)
    # submission.completed = True
    # submission.save()

    # Show a success message ++ NEED TO ADD SUBMISSION ID TO TRACK
    messages.success(request, 'Your submission has been successfully completed!')

    # later setup redirect to a specific URL or render a completion page:
    # return redirect('home')  # Redirect to home or another page
    return render(request, 'submit/submission_complete.html', {'submission': submission})

