from django.shortcuts import render
from .forms import CompanyForm

# Create your views here.
def Company_create_view(request):
	form = CompanyForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = CompanyForm()

	context = {
		'form': form
	}
	return render(request, "form/create.html", context)