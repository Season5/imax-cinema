from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^schedule/$', views.schedule, name="schedule"),
    url(r'^movie/(?P<id>[0-9]+)/$', views.movie, name="movie"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)