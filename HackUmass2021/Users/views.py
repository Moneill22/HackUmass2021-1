from django.shortcuts import render
from .models import User
from .forms import ProductForm

# Create your views here.


def User_create_view(request):
	form = UserForm(request.POST or None)

	if form.is_valid():
		form.save()
		form = UserForm()

	context = {
		'form': form
	}
	return render(request, "user/create.html", context)