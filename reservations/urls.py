from django.conf.urls import url, include
from reservations import views
from django.views.generic import DetailView
from .models import Movie
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^accounts/$', views.accountsview, name="accounts"),
    url(r'^accounts/login/$', views.login_view, name="login"),
    url(r'^accounts/auth/$', views.auth_view, name="auth"),
    url(r'^accounts/logout/$', views.logout_view, name="logout"),
    url(r'^accounts/loggedin/$', views.loggedin_view, name="loggedin"),
    url(r'^accounts/invalid/$', views.invalidlogin_view, name="invalidlogin"),
    url(r'^accounts/register/$', views.register_user_view, name="register user"),
    url(r'^accounts/register_success/$', views.registersuccess_view, name="register success"),
    url(r'^movies/$', views.moviesview, name="movies"),
    url(r'^movies/(?P<pk>\d+)$', DetailView.as_view(model=Movie, template_name="home/description.html"),
        name="movie_description"),
    url(r'^screenings', views.screening_view, name='screenings'),
    url(r'^tickets/$', views.ticketsview, name="tickets"),
    url(r'^vue$', views.vue_view, name="vue"),
    url(r'^tickets/cancel', views.ticketcancel_view, name="ticket_cancel"),
    url(r'^contact', views.contactview, name="contact"),
    url(r'^thegame', views.thegame_view, name="contact"),
    url(r'^ajax', views.ajaxview, name="ajax"),
    url(r'^vueopinion', views.vue_comment_view, name="ajax"),
    url(r'^api/', include(router.urls)),
    url(r'^evaluate', views.evaluateview, name="evaluate"),
    url(r'^addcommentvue', views.comment, name="addcommentvue"),
    url(r'^evaluate/(?P<id>\d+)/$', views.evaluateview, name="evaluateupdate"),
    url(r'^$', views.homeview, name="home"),
    url(r'^home/$', views.homeview, name="home1"),
]
