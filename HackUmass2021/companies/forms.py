from django import forms
from .models import User

class CompanyForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
            'name',
            'info',
		]
