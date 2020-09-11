from django.shortcuts import render

def home_view(request, *args, **kwargs):
    return render(request, 'home.html', {})

def nevbar_view(request, *args, **kwargs):
    return render(request, 'nevbar.html', {})

def contact_view(request, *args, **kwargs):
    return render(request, 'contact.html', {})

