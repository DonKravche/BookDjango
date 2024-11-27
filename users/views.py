from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import logout

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.save()
            return redirect('Book:index')
        else:
            return render(request, 'registration/registration.html', {"form": form})
    else:
        form = RegistrationForm()
        return render(request, 'registration/registration.html', {"form": form})


def log_out(request):
    logout(request)

    return redirect('Book:index')