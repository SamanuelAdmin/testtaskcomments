from django.urls import path, re_path

from . import views as mainviews


urlpatterns = [
    path('', mainviews.index, name='home'),
    path('<int:page>/', mainviews.index),
    path('add/', mainviews.addComment, name='add'),
]
