from django.shortcuts import render, redirect
from django.http import (
	HttpResponse, HttpRequest,
	HttpResponseNotFound, Http404
)

from .models import Comment
from .forms import AddCommentForm


# Create your views here.
def index(request: HttpRequest, page=1) -> HttpResponse:
	if page < 1: raise Http404()

	allMainComments = Comment.objects.filter(parentComment=None) # Comment.objects.all()

	sortingType = request.GET.get('s')
	if sortingType:
		try: allMainComments = allMainComments.order_by(sortingType)
		except: pass

	# adding form for leave some comments
	if request.POST:
		addCommentsForm = AddCommentForm(request.POST)
		if addCommentsForm.is_valid():
			replyID = request.POST.get('replyID')

			if replyID:
				savedComment = addCommentsForm.save(commit=False) # dont save
				savedComment.parentComment = Comment.objects.get(pk=replyID)

			addCommentsForm.save()
			addCommentsForm.clean() # returning clear form
	else:
		addCommentsForm = AddCommentForm()

	inpageData = {
		'page': page,
		'comments': allMainComments,
		'commentsCount': len(allMainComments),
		'sortingType': sortingType,
		'addCommentsForm': addCommentsForm
	}

	return render(
		request, 'main/index.html',
		inpageData
	)
  
def addComment(request: HttpRequest) -> HttpResponse:
	return HttpResponse('Add') # redirect('home')

def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Page not found</h1>')