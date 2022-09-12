from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from custom_user.models import CustomUser
from bugtracker.settings import AUTH_USER_MODEL
from .forms import SignUpForm, LoginForm
# Create your views here.

def login_view(request):
    """Login View"""
    # if request.user.is_authenticated:
    #     return HttpResponseRedirect(reverse('home'))
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # breakpoint()
        # print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    form = LoginForm()

    return render(request, 'form.html', {'form': form})

@login_required
def signup_view(request):
    """Sign Up View"""
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create(
                username=data['username'],
                password=data['password'],
            )
            login(request, user)
            return HttpResponseRedirect(reverse('home'))

    form = SignUpForm()

    return render(request, 'form.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))