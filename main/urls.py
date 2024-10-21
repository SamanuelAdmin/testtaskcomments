from django.urls import path, re_path, include

from . import views as mainviews


urlpatterns = [
    path('', mainviews.index, name='home'),
    path('<int:page>/', mainviews.index),
    path('captcha/', include('captcha.urls')),
]
