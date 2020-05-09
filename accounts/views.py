from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
	###SUBMITING SIGN UP FORM###
	if request.method == 'POST':
		#user entered info and submittes
		for detail in request.POST:
			if len(detail) > 14:
				return render(request, 'signup.html',{'error':'One of the details you entered is too long, must be less than 14 charachters'})

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
	if request.method == 'POST':
		user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			auth.login(request, user)
			return redirect('home')
		else:
			return render(request, 'login.html',{'error':'User does not exist, please check password and try again.'})
	else:
		return render(request, 'login.html')

def logout(request):
	if request.method == 'POST':
		auth.logout(request) 
		return redirect('home')