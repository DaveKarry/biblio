from django.db import models
from django.urls import reverse


# Create your models here.
class Genre(models.Model):
    """
    Модель жанра книги, например: научная фантастика, детектив
    """
    name = models.CharField(max_length=200, help_text="Введите название жанра")

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Модель книги
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Небольшое ревью книги")
    genre = models.ManyToManyField(Genre, help_text="Выберите жанр книги")


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])


class Author(models.Model):
    """
    Модель автора
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])


    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)
