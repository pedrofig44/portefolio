from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Add your contact form processing logic here
        # For example, sending an email or saving to database
        messages.success(request, 'Your message has been sent!')
        return redirect('contact')
    return render(request, 'contact.html')