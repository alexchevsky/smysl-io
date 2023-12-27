from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required

from .forms import RegistrationForm, CustomAuthenticationForm

@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='/login/')
def my(request):
    return render(request, 'my.html')

def register(request):
    # Assuming you have a form class named RegistrationForm
    # from .forms import RegistrationForm

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('registration_success')  # Redirect to a success URL
    else:
        form = RegistrationForm()  # Empty form for GET request

    return render(request, 'register.html', {'form': form})

def registration_success(request):
    return render(request, 'registration_success.html')

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')  # Assuming your user model uses 'email' field as 'username'
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                # Redirect to the 'next' parameter or, if not present, to the home page
                next_url = request.GET.get('next', 'home_page')
                return redirect(next_url)
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})