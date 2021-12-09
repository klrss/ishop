from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# form to login users using class

class LoginForm(forms.Form):
	username = forms.CharField(max_length=63)
	password = forms.CharField(max_length=63,widget=forms.PasswordInput)

# form to registrate users using classn	
class NewUserForm(UserCreationForm):
	firstname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	lastname = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	#password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
	#password2 =forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm password'}))

	class Meta:
		model = User
		fields = ['username','firstname','lastname','email','password1','password2']

	#  
	def save(self, commit=True):
		user = super(NewUserForm,self).save(commit=False)
		user.firstname = self.cleaned_data['firstname']
		user.lastname = self.cleaned_data['lastname']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
