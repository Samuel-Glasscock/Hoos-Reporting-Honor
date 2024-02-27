from django.shortcuts import render

# Create your views here.
def home(request):
    if request.user.profile.is_admin:
        return render(request, "login/admin_home.html")
    elif request.user.is_authenticated:
        return render(request, "shared/common.html")
    return render(request, "404.html")