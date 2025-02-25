from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Service, Contact

def home(request):
    photos = Photo.objects.all()
    services = Service.objects.all()
    return render(request, 'home.html', {'photos': photos, 'services': services})

def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Contact.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')