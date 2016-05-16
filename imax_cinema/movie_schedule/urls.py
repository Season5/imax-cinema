from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^about/$', views.about, name="about"),
    url(r'^schedule/$', views.schedule, name="schedule"),
    url(r'^movie/(?P<id>[0-9]+)/$', views.movie, name="movie"),
    url(r'^seat_values/$', views.seat_values, name="seat_values"),
    url(r'^total_price/$', views.total_price, name="total_price"),
    url(r'^occupied_seat_val/$', views.occupied_seat_val, name="occupied_seat_val"),
]
if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)