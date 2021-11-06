from django import forms
from .models import User, Application

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'GPA',
			'NUMBER_OF_INTERNSHIPS',
			'DEGREE',
			'college',
		]

class AppsForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = [
			'user',
			'company',
			'response'
		]