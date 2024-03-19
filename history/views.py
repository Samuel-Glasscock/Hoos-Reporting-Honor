from django.shortcuts import render, redirect
from shared.models import Report
from .forms import CaseForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def lookup(request):
    if request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("user_password")
        report_model = Report.objects.get(id=id)
        if report_model.user.password == password:
            return redirect("history:case", id=id)
        return render(request, "history/lookup.html", {'form': CaseForm(), 'error': "Invalid password"})
    else:
        form = CaseForm()
    return render(request, "history/lookup.html", {'form': form})

def case(request, id):
    report_model = Report.objects.get(id=id)
    return render(request, "history/case.html", {"id": id, "report": report_model})
@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser:
        reports = Report.objects.all()
    else:
        reports = Report.objects.filter(user=user)
    return render(request, "history/dashboard.html", {'reports': reports})

def report(request, id):
    if request.method == "POST":
        report_model = Report.objects.get(id=id)
        # if its a text field called notes add and save
        if "notes" in request.POST:
            report_model.notes = request.POST.get("notes")
            report_model.save()
            return render(request, "history/report.html", {"report": report_model, "message": "Notes saved"})
        # if its a bool field for resolved update field
        if "resolved" in request.POST:
            report_model.status = "APPROVED"
            report_model.save()
            return render(request, "history/report.html", {"report": report_model, "message": "Resolved status saved"})


    report_model = Report.objects.get(id=id)
    return render(request, "history/report.html", {"report": report_model})
