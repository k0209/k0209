from django.conf.urls import url
from RestaurantApp import views
from django.conf.urls.static import static
from django.conf import settings 



urlpatterns = [   
url(r'reservation/$',views.reservationApi),
url(r'^reservation/([0-9]+)$',views.reservationApi),

url(r'^SaveFile$', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
