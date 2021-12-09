from django.contrib.auth import authenticate, login, logout
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib import messages

def login_page(request):
	form=forms.LoginForm()
	message = ''
	#create an instance of login form and fill it with data from request
	if request.method == 'POST':
		form = forms.LoginForm(request.POST)
		#check if valid
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				message=f"Hello {user.username}! You are now logged in."
				#redirect to a success page
			else:
				message= "Invalid username or password"
		
	return render(request,'login.html',{'form':form,'message':message})

# registration 
def register(request):
	if request.method=='POST':
		form = forms.NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect('login.html')
	
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = forms.NewUserForm()
	return render(request,'register.html',{'form':form})

def logout_user(request):
	logout(request)
	return redirect('login')