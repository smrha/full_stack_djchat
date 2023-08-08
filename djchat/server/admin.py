from django.contrib import admin

from .models import Server, Category, Channels

admin.site.register(Server)
admin.site.register(Channels)
admin.site.register(Category)