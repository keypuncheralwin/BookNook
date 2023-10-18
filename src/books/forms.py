from django import forms
from . models import BookTitle
from django.core.exceptions import ValidationError

class BookTitleForm(forms.ModelForm):
    class Meta:
        model = BookTitle
        fields = ('title', 'publisher', 'author')

    def clean(self):
        title = self.cleaned_data.get('title')

        if len(title) < 3:
            error_msg = 'the title is too short'
            self.add_error('title', error_msg)
            # raise ValidationError(error_msg)

        book_title_exists = BookTitle.objects.filter(title__iexact=title).exists()

        if book_title_exists:
            self.add_error('title', 'This book title already exists')

        return self.cleaned_data

