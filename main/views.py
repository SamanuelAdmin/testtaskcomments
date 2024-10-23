from django.shortcuts import render, redirect
from django.http import (
	HttpResponse, HttpRequest,
	HttpResponseNotFound, Http404
)
from django.core.paginator import Paginator, EmptyPage

from .models import Comment
from .forms import AddCommentForm

from .modules import permitted_html_elements



def getAddingForm(request):
	# adding form for leave some comments
	if request.POST:
		addCommentsForm = AddCommentForm(request.POST, request.FILES)
		if addCommentsForm.is_valid():
			replyID = request.POST.get('replyID')

			if replyID:
				savedComment = addCommentsForm.save(commit=False) # just get obj, dont save

				if savedComment: # if data was validate
					savedComment.parentComment = Comment.objects.get(pk=replyID)

			# need try/except only for not validate data situations
			try: addCommentsForm.save()
			except ValueError: pass
			addCommentsForm.clean() # returning clear form
	else:
		addCommentsForm = AddCommentForm()

	return addCommentsForm


def addPaginator(allObjects, page, elemOnPage=10):
	try:
		paginator = Paginator(allObjects, elemOnPage)
		return paginator.page(page)
	except EmptyPage: raise Http404()


# Create your views here.
def index(request: HttpRequest, page=1) -> HttpResponse:
	if page < 1: raise Http404()

	allMainComments = Comment.objects.filter(parentComment=None)

	sortingType = request.GET.get('s')
	if sortingType:
		try: allMainComments = allMainComments.order_by(sortingType)
		except: pass

	commentsPage = addPaginator(allMainComments, page, elemOnPage=20)


	return render(
		request, 'main/index.html',
		{
			'page': page,
			'comments': commentsPage,
			'sortingType': sortingType,
			'addCommentsForm': getAddingForm(request),
			'instrumentMenu': permitted_html_elements.permittedTags
		}
	)


def page_not_found(request, exception):
	return HttpResponseNotFound('<h1>Page not found</h1>')