from django.http import HttpResponse
from django.shortcuts import render

def home_page_old(request):
    return HttpResponse("Hello World")

def home_page(request):
    data = {
        'title': 'Hello World!',
        'content': 'Welcome to the Home Page.'
    };
    return render(request, "home_page.html", context=data)

def about_page(request):
    data = {
        'title': 'About Page'
    };
    return render(request, "about_page.html", context=data)

def contact_page(request):
    data = {
        'title': 'Contact Page',
        'content': 'Welcome to the Contact Page.'
    };
    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('full_name'))
        print(request.POST.get('email'))
        print(request.POST.get('content')) 

    return render(request, "contact/view.html", context=data)
