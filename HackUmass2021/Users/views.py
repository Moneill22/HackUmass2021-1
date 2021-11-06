from django.shortcuts import render
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