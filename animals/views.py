from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from accounts.models import User
from . models import Pet
from accounts.forms import  UserForm
from django.contrib import auth
from .forms import PetForm

# Create your views here.


def home(request):
    pets = Pet.objects.all()
    context = {
        'pets': pets
    }
    return render(request, 'home.html', context)


# Create your views here.

def RegisterUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
            user.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = UserForm()
    context = {
        'form':form,
    }
    return render (request, 'accounts/registerUser.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect ('home')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        """
        Use Django inbuilt authenticate function
        """
        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            return redirect('login')
    return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='login')
def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('home')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})