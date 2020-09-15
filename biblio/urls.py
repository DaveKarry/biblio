from django.urls import include,path,re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.book_list, name='book_list'),
	re_path(r'^genre/list/$', views.genre_list, name='genre_list'),
	re_path(r'^author/list/$', views.author_list, name='author_list'),
	re_path(r'^book/new/$', views.book_new, name='book_new'),
	re_path(r'^genre/new/$', views.genre_new, name='genre_new'),
	re_path(r'^author/new/$', views.author_new, name='author_new'),
]
