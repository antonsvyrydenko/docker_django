from django.urls import path
from . import views

urlpatterns = [
	path(r'', views.index, name='index'),
	path(r'search_authors/', views.search_authors),
	path(r'search_books/', views.search_books),
]
