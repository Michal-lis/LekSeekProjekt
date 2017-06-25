from django.conf.urls import url
from reservations import views
from django.views.generic import DetailView
from .models import Movie

urlpatterns = [
    # urls for logging in
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
    url(r'^tickets/cancel', views.ticketcancel_view, name="ticket_cancel"),
    url(r'^contact', views.contactview, name="contact"),
    url(r'^$', views.homeview, name="home"),
    url(r'^home/$', views.homeview, name="home1"),
]
