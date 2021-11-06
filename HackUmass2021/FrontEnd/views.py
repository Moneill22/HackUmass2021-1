from django.shortcuts import render
from Users.models import User, Application
from companies.models import Company

# Create your views here.

def index(request):
    return render(request, 'landing.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def dashboard(request, user_id):
    # at most 3 most recent applications, at most 3 company recommendations
    NUM_APPS = 3
    user = User.objects.get(id=user_id)
    applications = Application.objects.filter(user=user)
    
    app_context = {}
    # rec_context = {} # TODO add company recs

    for app in applications:
        if len(app_context) == NUM_APPS:
            break
        app_context.update({app.company_id : app.response})


    context = app_context # TODO add company recs
    print(context)
    return render(request, 'dashboard.html', context)

