from django.shortcuts import render
from companies.views import add_user_to_graph
from .models import User
from .forms import UserForm

# Create your views here.


def User_profile_view(request):
	form = UserForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = UserForm()

	context = {
		'form': form
	}
	return render(request, "create.html", context)

def App_creation_view(request):
	
	if requestion.method == 'POST':
		company_id = request.POST['company_id']
		response = request.POST['response']
		try:
			company = Company.objects.get(name=company_id)
			user = User.objects.get(username=request.user.username)
			app = Application(user = user, company_id = company_id, response = Response_Int(response))
			add_user_to_graph(request.user.username, company_id)
		except:
			return 0
		

		context = {
			'user': User.objects.get(username=request.user.username),
			'company_id': request.POST['company_id'],
			'response': response
		}

	return render(request, "app_create.html", context)

def App_update_view(request):

	if request.method == 'PATCH':

		app = Application.objects.get(User.get(username = request.user.username))
		app.response = request.POST['response']
		app.save(update_fields=['response'])
	
	context = {
		'user': app.user,
		'company_id':  app.company_id,
		'response': app.response
	}

	return render(request, "app_create.html", context)

def Response_Int(response):
	if response == "":
		return 0 #offer
	elif response == "":
		return 1 #Interview
	elif response == "":
		return 2 #ghosted
	else:
		return 3 #pending
