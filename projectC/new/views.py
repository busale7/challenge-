from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render ,redirect
from django.http  import HttpResponse
from .models import Challenge
from .forms import ChallengeForm ,SignupForm, LoginForm
from django.contrib.auth import authenticate , login ,logout
# Create your views here.
def challengeList(request):
	mychallenge = Challenge.objects.all()
	context ={
		'mychallenge': mychallenge 
	}
	return render(request,'list.html', context)

def detialList(request,challenge_id): 
 	context ={
 		"mychallenge" : Challenge.objects.get(id=challenge_id),


 	}
 	return render(request,"detail.html", context)

def create(request):
	form = ChallengeForm()
	if request.method =="POST" :
		form = ChallengeForm(request.POST, request.FILES or None)
		if form.is_valid():
			form.save()
			return redirect('list_challenge')
	context ={
		'form': form
	}
	return render(request, 'create.html', context)

def update(request, challenge_id):
	challenge = Challenge.objects.get(id = challenge_id)
	form = ChallengeForm(instance = challenge)
	if request.method =="POST" :
		form = ChallengeForm( request.POST, request.FILES or None, instance=challenge)
		if form.is_valid():
			form.save()
			return redirect('detail' ,challenge_id=challenge.id)
	context ={
		'challenge':challenge,
		'form': form,
		
	}
	return render(request, 'update.html', context)

def delete(request, challenge_id):
	challenge = Challenge.objects.get(id=challenge_id)
	challenge.delete()
	return redirect('list_challenge')

def signup(request):
	form =SignupForm()
	if request.method =="POST":
		form = SignupForm(request.POST)
		if form.is_valid():   #request.method =="POST":
			user =form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect("list_challenge")
	context ={
		"form":form
	}
	return render(request, 'signup.html', context)

def user_login(request):
	form = LoginForm()
	if request.method =="POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			authen = authenticate(username=username ,password=password)
			if authen is not None:
				login(request, authen)
				return redirect("list_challenge")
	context ={
		"form":form
	}
	return render(request, 'login.html', context)
def user_logout(request):
	logout(request)
	return redirect('login')


