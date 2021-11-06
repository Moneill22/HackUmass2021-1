from django.shortcuts import render
from .forms import CompanyForm
from Users.models import User
from .models import Company, Graph

# Create your views here.
def Company_create_view(request):
	form = CompanyForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = CompanyForm()

        # init graph
        graph = Graph(company=form.id) 
        graph.save()
	context = {
		'form': form
	}
	return render(request, "form/create.html", context)

def add_user_to_graph(user_id, company):
    try:
        user = User.objects.get(id=user_id)
        graph = Graph.objects.get(company=company)
        graph.users.add(user)
    except:
        return 'No user/graph with that id found'

def get_graph_info(company):
    pass
