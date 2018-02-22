from django import forms
from django.contrib.auth.models import User

from .models import Challenge #importing the class Business from models.py
#from django.contrib.auth.models import User

class ChallengeForm(forms.ModelForm):
	class Meta : 
		model = Challenge 
		fields ='__all__'

class SignupForm(forms.ModelForm) :
	class Meta:
		model = User 
		fields =['username','email','first_name','last_name','password']
		widgets= {
			"password": forms.PasswordInput()
		}
		
class LoginForm(forms.Form) :
	username = forms.CharField(required=True)
	password = forms.CharField(required=True , widget=forms.PasswordInput())