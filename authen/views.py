from django.shortcuts import render, redirect
from django.views.generic import FormView
from authen.forms import LoginForm, RegisterForm
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


class LoginView(FormView):
    template_name = 'auth.html'
    # success_url = '/qna'
    form_class = LoginForm

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            messages.success(request, "login success")
            return redirect(reverse('qna:index'))

        messages.error(request, "username or password is incorrected")
        return redirect('/login')


class RegisterView(FormView):
    template_name = 'auth.html'
    # success_url = '/qna'
    form_class = RegisterForm

    def post(self, request):
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "registration successful")
            return redirect(reverse('qna:index'))

        messages.error(request, "there are something wrong")
        return redirect('/register')


def log(request):
    logout(request)
    return redirect(reverse('qna:index'))
