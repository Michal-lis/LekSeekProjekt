from django.conf.urls import url, include
from django.contrib import admin
from reservations import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.homeview, name="home"),
    # url(r'^home/$',views.homeview,name="home"),
    url(r'^', include('reservations.urls', namespace='reservations'))
]
