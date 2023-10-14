from django.contrib import admin
from books.models import Book, BookTitle

# Register your models here.
admin.site.register(BookTitle)
admin.site.register(Book)
