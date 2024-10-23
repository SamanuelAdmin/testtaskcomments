from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views as mainviews


urlpatterns = [
    path('', mainviews.index, name='home'),
    path('<int:page>/', mainviews.index, name="onpage"),
    path('captcha/', include('captcha.urls')),
]

if settings.DEBUG: # for getting media files from MEDIA_ROOT in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)