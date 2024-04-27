from django.contrib import admin
from.models import Category, Post, Brands

admin.site.register((Category, Post, Brands))

