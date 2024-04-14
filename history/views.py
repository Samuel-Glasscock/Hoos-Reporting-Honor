from django.shortcuts import render, redirect, get_object_or_404
from shared.models import Report
from .forms import CaseSearchForm
from django.contrib.auth.decorators import login_required
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

@login_required
@require_POST
def report(request, id):
    report_model = get_object_or_404(Report, id=id)

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
            return redirect("history:report_details", id=id)

    return render(request, "history/report_details.html", {"report": report_model})

def delete(request, id):
    report_model = Report.objects.get(id=id)
    report_model.delete()
    return redirect("history:dashboard")
