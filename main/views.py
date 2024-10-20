from django.shortcuts import render, redirect
from django.http import (
	HttpResponse, HttpRequest,
	HttpResponseNotFound, Http404
)

from .models import Comment



# Create your views here.
def index(request: HttpRequest, page=1) -> HttpResponse:
	if page < 1: raise Http404() 

	allMainComments = Comment.objects.filter(parentComment=None) # Comment.objects.all()

	inpageData = {
		'page': page,
		'comments': allMainComments,
		'commentsCount': len(allMainComments)
	}

	return render(
		request, 'main/index.html',
		inpageData
	)
  
def addComment(request: HttpRequest) -> HttpResponse:
	return HttpResponse('Add') # redirect('home')

def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Page not found</h1>')