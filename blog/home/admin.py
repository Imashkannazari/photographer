from django.contrib import admin
from .models import Photo, Service, Contact, Category


admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Contact)
admin.site.register(Service)
