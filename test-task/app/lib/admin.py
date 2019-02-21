from django.contrib import admin

from .models import Author, Book
from django.contrib.admin.models import LogEntry

# Register your models here.

admin.site.register(LogEntry)
admin.site.register(Author)
admin.site.register(Book)
