from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User, auth

# Create your views here.
def login_(request, *args, **kwargs):
	if request.method == "POST":
		username = request.POST.get('username').strip()
		password = request.POST.get('password').strip()

		user = authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('packages')
		else:
			messages.error(request, "whoops! invalid username or password...")
			return redirect('/')
			
	else:
		return render(request, "login.html")
	
def register(request, *args, **kwargs):
	if request.method == "POST":
		first_name = request.POST.get('firstname').strip().capitalize()
		last_name = request.POST.get('lastname').strip().capitalize()
		username = request.POST.get('username').strip().lower()
		password1 = request.POST.get('password1').strip()
		password2 = request.POST.get('password2').strip()
		email = request.POST.get('email').strip()

		if password1 == password2:
			if User.objects.filter(username=username).exists():
				messages.info(request, "whoops! username taken, try another...")
				return redirect('/')
			elif User.objects.filter(email=email).exists():
				messages.info(request, "whoops! Email already in use...")
				return redirect('/')
			else:
				user = User.objects.create_user(username=username, password=password1,email=email,first_name=first_name,last_name=last_name)
				user.save()

				user = authenticate(username=username, password=password1)
				login(request, user)

				return redirect('/')
		else:
			messages.info(request, "whoops! passwords not matching...")
			return redirect('/')

	else:
		return render(request, "register.html")


def logout_(request, *args, **kwargs):
	logout(request)
	return redirect('/')