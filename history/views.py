from django.shortcuts import render, redirect, get_object_or_404
from shared.models import Report
from .forms import CaseSearchForm
from django.contrib.auth.decorators import login_required, profile_is_admin
from django.views.decorators.http import require_POST


def lookup(request):
    if request.method == "POST":
        form = CaseSearchForm(request.POST)
        if form.is_valid():
            uuid = form.cleaned_data['report_hash']
            report = get_object_or_404(Report, report_hash=uuid)
            return render(request, "history/report_details.html", {"report": report})
        else:
            return render(request, "history/lookup.html", {'form': form, 'error': "Invalid case ID"})
    else: 
        form = CaseSearchForm()
        return render(request, "history/lookup.html", {'form': form})


def case(request, case_hash):
    report_model = get_object_or_404(Report, case_hash=case_hash)
    return render(request, "history/case.html", {"id": id, "report": report_model})

@login_required
def dashboard(request):
    profile = request.user.profile
    user = request.user
    if user.is_superuser:
        reports = Report.objects.filter(user=user)
    elif hasattr(user, 'profile') and profile.is_admin:
        reports = Report.objects.all()
    else:
        reports = Report.objects.filter(user=user)
    return render(request, "history/dashboard.html", {'reports': reports})

@login_required and profile_is_admin
@require_POST
def report(request):
    report_id = request.POST.get('report_id')
    # handle case where no report ID is found in the session
    if not report_id:
        return redirect("history:dashboard")
    
    report_model = get_object_or_404(Report, id=report_id)

    if request.method == "POST":
        if "notes" in request.POST:
            report_model.report_text = request.POST.get("notes")
            report_model.save()
            return redirect("history:report", id=id)
        if "status" in request.POST:
            report_model.status = "APPROVED"
            report_model.save()
            return redirect("history:dashboard")
        if "change_status_to_pending" in request.POST:
            report_model.status = "PENDING"
            report_model.save()
            
        # if change_status_to_rejected in request.POST:    
        # have some post request to change the status of the report to rejected in 
        # then change status to "REJECTED"
        # then save 

    request.session['viewing_report_id'] = str(report_model.id)
    return redirect("history:report_details")

def report_details(request):
    report_id = request.session.get('viewing_report_id')
    if not report_id:
        # Handle case where no report ID is found in the session?
        return redirect("history:dashboard")

    report_model = get_object_or_404(Report, id=report_id)
    del request.session['viewing_report_id']
    return render(request, "history/report_details.html", {"report": report_model})

@login_required
@require_POST
def delete(request):
    report_id = request.POST.get('report_id')
    if report_id:
        report = get_object_or_404(Report, id=report_id)
        report.delete()
        return redirect("history:dashboard")
    else:
        return redirect("history:dashboard") 
