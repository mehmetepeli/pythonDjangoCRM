from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm

def home(request):
    # Check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have been login!")
            return redirect('home')
        else:
            messages.success(request, "There is an error logging in, Please try again...")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

def reqister_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()

            # Authenticate and login
            username = new_user.cleaned_data['username']
            password = new_user.cleaned_data['password']
            user = authenticate(username=username, password=password)

            # Login
            login(request, user)
            messages.success(request, "You Have Successfully Registered! Welcome!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logout!")
    return redirect('home')

