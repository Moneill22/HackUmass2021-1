from django import forms
from .models import User

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'GPA,
			'internships',
			'degree',
			'college',
			'interview_skill',
			'projects'
		]
