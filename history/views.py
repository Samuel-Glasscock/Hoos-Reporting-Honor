from django.shortcuts import render, redirect
from shared.models import Report
from .forms import CaseForm

# Create your views here.

def lookup(request):
    if request.method == "POST":
        id = request.POST.get("id")
        password = request.POST.get("user__password")
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