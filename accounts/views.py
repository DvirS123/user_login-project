from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	###SUBMITING SIGN UP FORM###
	if request.method == 'POST':
		#user entered info and submittes
		if request.POST['password1'] == request.POST['password2']:
			#if passwords match
			try:
				user = User.objects.get(username = request.POST['username'])
				return render(request, 'signup.html',{'error':'Username already exists!'})

			except User.DoesNotExist:
				user = User.objects.create_user(request.POST['username'],password = request.POST['password1'])
				auth.login(request,user) 
				return redirect('home')

		else:
			 return render(request, 'signup.html',{'error':'Passwords must match'})
	return render(request, 'signup.html')

def login(request):
	return render(request, 'login.html')

def logout(request):
	pass
	#return render(request, '')