from django import forms
from .models import User, Application

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'username',
			'GPA',
			'MONTHS_INTERNING',
			'college',
		]

class AppsForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = [
			'user',
			'company_id',
			'response'
		]