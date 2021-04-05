from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm


def home_page_old(request):
    return HttpResponse("Hello World")

def home_page(request):
    data = {
        'title': 'Hello World!',
        'content': 'Welcome to the Home Page.'
    };

    if request.user.is_authenticated:
        data['premium_content'] =  'This is the content for premium members.'

    return render(request, "home_page.html", context=data)

def about_page(request):
    data = {
        'title': 'About Page'
    };
    return render(request, "about_page.html", context=data)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    data = {
        'title': 'Contact Page',
        'content': 'Welcome to the Contact Page.',
        'form': contact_form
    };
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context=data)

def login_page(request):
    form = LoginForm(request.POST or None)
    data = {
        'form': form
    }
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user = authenticate(request, username=username, password=password)
            # data['form'] = LoginForm()
            return redirect('/login')
        else:
            # Return an 'invalid login' error message.
            print("Error")
    return render(request, 'auth/login.html', context=data)

def register_page(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'auth/register.html', {})
