from django.shortcuts import render, redirect
from shared.models import Report
# Create your views here.

def lookup(request):
    if request.method == "POST":
        id = request.POST.get("id")
        return redirect("history:case", id=id)
    return render(request, "history/lookup.html")

def case(request, id):
    report_model = Report.objects.get(id=id)
    return render(request, "history/case.html", {"id": id, "report": report_model})