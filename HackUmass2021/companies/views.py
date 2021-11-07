from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import CompanyForm
from Users.models import User, Application
from .models import Company, Graph

# Create your views here.
def Company_create_view(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = CompanyForm()
        # init graph
        graph = Graph(company_id=form.name)
        graph.save()
    context = {
		'form': form
	}
    return render(request, "form/create.html", context)

def company_profile_view(request, company_id):
    try:
        company = Company.objects.get(name=company_id)
        context = {}
        context.update({'name': company.name})
        context.update({'info': company.info})
        context.update({'graph': get_graph_info(company.name)})

        return render(request, "Company.html", context)
    except:
        return 0

#Helper Functions
def add_user_to_graph(username, company_name):
    try:
        user = User.objects.get(username=username)
        graph = Graph.objects.get(company_id=company_name)
        graph.users.add(user)
    except:
        return 'No user/graph with that id found'

def get_graph_info(company_id):
    try: 
        graph = Graph.objects.get(company_id=company_id)
        users = graph.users.all()
        info = []
        for user in users:
            app = Application.objects.get(user=user)
            point = {
                "user" : user.username,
                "status" : app.response,
                "GPA" : user.GPA,
                "Months_interning" : user.MONTHS_INTERNING 
            }
            info.append(point)
        return info
    except:
        return 'Company or Application not found'

# After graph click ?
def redirect_to_user_account(request, user_id):
    return HttpResponseRedirect(f'/account/{user_id}')
def redirect_to_company_page(request, company_id):
    return HttpResponseRedirect(f'/account/{company_id}')