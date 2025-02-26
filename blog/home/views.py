from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Photo, Service, Contact, Category
from .forms import PhotoForm

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


def gallery(request):
    category = request.GET.get('category')
    if category:
        photos = Photo.objects.filter(category__name=category)
    else:
        photos = Photo.objects.all()

    categories = Category.objects.all()
    return render(request, 'gallery.html', {'photos': photos, 'categories': categories})

def photo_detail(request, photo_id):
    photo = get_object_or_404(Photo, id=photo_id)
    return render(request, 'photo_detail.html', {'photo': photo})


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')
    else:
        form = PhotoForm()
    return render(request, 'upload_photo.html', {'form': form})