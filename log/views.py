from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib import messages

def login_page(request):
	#create an instance of login form and fill it with data from request
	if request.method == 'POST':
		form = AuthenticationForm(request.POST)
		#check if valid
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username,password=password)
			if user is not None:
				login(request,user)
				messages.info(request,f"You are now logged in as {username}")
				#redirect to a success page
				return redirect("/")
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request,'login.html',{'form':form })

# registration 
def register(request):
	if request.method=='POST':
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful.")
			return redirect('login.html')
	
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render(request,'register.html',{'form':form})
