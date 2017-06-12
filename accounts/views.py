from django.shortcuts import render, redirect
from django.contrib.auth import (
	authenticate,
	get_user_model,
	login,
	logout,
	)

from .forms import UserLoginForm, UserRegisterForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

def home(request):
	return render(request, 'accounts/home.html')

def login_view(request):
	title = "Login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/account/")

	return render(request, "accounts/form.html", {'form':form, "title": title})

def logout_view(request):
	logout(request)
	return render(request, "accounts/logout.html", {})
	return redirect("/account/")

def register_view(request):
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		login(request, user)
		return redirect("/account/")


	context = {
		'form': form,
		'title': title,
	}
	return render(request, "accounts/form.html", context)

def profile_view(request):
	args = {'user': request.user}
	return render(request, "accounts/profile.html", args)

def edit_profile_view(request):
	if request.method =='POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile/')
	else:
		form = EditProfileForm(instance=request.user)
		args = {"form": form}
		return render(request, 'accounts/edit_profile.html', args)
from django.core.mail import send_mail

def message_view():
	if form.is_valid():
	    subject = form.cleaned_data['subject']
	    message = form.cleaned_data['message']
	    sender = form.cleaned_data['sender']
	    cc_myself = form.cleaned_data['cc_myself']

	    recipients = ['info@example.com']
	    if cc_myself:
	        recipients.append(sender)

	    send_mail(subject, message, sender, recipients)
	    return HttpResponseRedirect('/thanks/')

