from django import forms
from . models import BookTitle

class BookTitleForm(forms):
    class Meta:
        model = BookTitle
        fields = ('title', 'publisher', 'author')

