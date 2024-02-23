from django.shortcuts import render

def admin_home(request):
    #Add any logic needed here, such as fetching data from the database
    #pass an empty dictionary to the template
    context = {}
    return render(request, 'admin_home.html', context)

#Create views here
