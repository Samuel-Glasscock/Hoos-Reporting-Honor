from django.shortcuts import render

def anonymous_submission(request):
    if request.method == "POST":
        print(request.POST)
        # include logic for form here 
        return render(request, "anonymous_submission.html", {})
