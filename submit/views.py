from django.shortcuts import render, redirect


# Create your views here.
def StartSubmitView(request):
    return render(request, "submit/start_submission.html")


def BackgroundInfoView(request):
    return render(request, "submit/background_info.html")


def InvolvedStudentsView(request):
    return render(request, "submit/involved_students.html")


'''
def submit_form(request):
    need to set up later
'''
