from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from Users.models import User, Application
from companies.models import Company
from Users.views import init_user_profile, update_user_profile

# Create your views here.

def index(request):
    if request.user != None and request.user.username != 'admin':
        return HttpResponseRedirect(f'dashboard/{request.user.username}')    
    return render(request, 'landing.html')

# def signup(request):
#     return render(request, 'signup.html')

# def signin(request):
#     return render(request, 'signin.html')

def dashboard(request, username):
    # at most 3 most recent applications, at most 3 company recommendations
    # NUM_APPS = 3
    if len(User.objects.filter(username=username)) == 0:
        init_user_profile(username)
    profile = User.objects.filter(username=username)[0] # TODO bug?
    applications = Application.objects.filter(user=profile).all()

    context = {'user' : profile, 'apps' : applications} # TODO add company recs
    return render(request, 'profile.html', context)

def update_dashboard(request, username):
    if request.method == 'POST':
	    user_profile = User.objects.get(username = username)
	    user_profile.GPA = request.POST.get('gpa', '')
	    user_profile.MONTHS_INTERNING = request.POST.get('internship-months', '')
	    user_profile.college = request.POST.get('education', '')
	    user_profile.save(update_fields=['GPA', 'MONTHS_INTERNING', 'college'])
    return HttpResponseRedirect(f'../dashboard/{username}')