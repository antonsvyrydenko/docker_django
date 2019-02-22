from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Author, Book
import re

def index(request):
 	return render(request, 'lib/index.html')

def search_authors(request):
	result=[]
	if 'authors_names' in request.GET:
		fname=request.GET['author_firstname']
		if fname and not (re.search(r'\d', fname)):
			auths = Author.objects.all().filter(name__contains=fname)
			for e in auths:		
				result.append(e)
		else:
			error_message='Empty field / Invalid input'
			return render(request, 'lib/index.html', {'error_message':error_message})

	if 'authors_list' in request.GET:
		try:
			order_param=request.GET['order']
			order=''
			if order_param=='desc':
				order='-'
			auths = Author.objects.order_by(order+'name')
			for e in auths:		
				result.append(e)
		except:
			error_message='Select order for results!'
			return render(request, 'lib/index.html', {'error_message':error_message})

	return render(request, 'lib/index.html', {'result':result})

def search_books(request):
	result__=[]
	if 'book_list' in request.GET:
		try:
			order_param=request.GET['order']
			sort=request.GET['b_order']
			order=''
			if order_param=='desc':
				order='-'
			books = Book.objects.order_by(order+sort)
			for e in books:		
				result__.append(e)
		except:
			error_message='Select order and sort parameter!'
			return render(request, 'lib/index.html', {'error_message':error_message})

	if 'book_info' in request.GET:
		title=request.GET['book_title']
		if title:
			books = Book.objects.all().filter(title__contains=title)
			for e in books:		
				result__.append(e)
		else:
			error_message='Specify book title!'
			return render(request, 'lib/index.html', {'error_message':error_message})

	if 'book_author' in request.GET:
		fname=request.GET['author_firstname']
		if fname and not (re.search(r'\d', fname)):
			books=Book.objects.filter(author__name__contains=fname).distinct()
			for e in books:		
				result__.append(e)
		else:
			error_message='Empty field / Invalid input'
			return render(request, 'lib/index.html', {'error_message':error_message})

	return render(request, 'lib/index.html', {'result__':result__})
