from django import forms
from .models import Book,Author,Genre


class Book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author','summary','genre',)
class Author_form(forms.ModelForm):
    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth', 'date_of_death',)
class Genre_form(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ('name',)
