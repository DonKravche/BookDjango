from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import FormView

from .forms import RegistrationForm
from django.contrib.auth import logout, login
from django.urls import reverse_lazy

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


class RegisterView(FormView):
    form_class = RegistrationForm
    template_name = 'registration/registration.html'
    success_url = reverse_lazy('Book:index-cbv')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def log_out(request):
    logout(request)

    return redirect('Book:index')


class LogOutView(FormView):
    @staticmethod
    def post(request, *args, **kwargs):
        logout(request)
        return redirect('/users/login/')