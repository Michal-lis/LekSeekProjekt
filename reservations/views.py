from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import csrf
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.core import serializers  # to jest potzrebne do wyswietlania przy metodzie Ajax
from reservations.models import Evaluation
from django.contrib.auth.models import User
from .serializers import CommentsSerializer
from rest_framework import viewsets
from .models import *


def homeview(request):
    return render(request, 'home/home.html')


def moviesview(request):
    movies = Movie.objects.all()
    return render(request, 'home/movies.html', {'movies': movies})


def ticketsview(request):
    if request.user.is_authenticated():
        user = User.objects.get(id=request.user.id)
        if request.method == 'GET':
            tickets = Ticket.objects.filter(user=user)
            return render(request, 'home/tickets.html', {'tickets': tickets})
        elif request.method == 'POST':
            screening_id = int(request.POST.get('screening_id'))
            how_many = int(request.POST.get('how_many'))
            screening = Screening.objects.get(id=screening_id)
            for _ in range(how_many):
                # seat = random.randint(1, 100)
                Ticket(screening=screening, user=user).save()
            return HttpResponseRedirect(reverse('reservations:tickets'))
    else:
        return render(request, 'home/tickets.html')


def ticketcancel_view(request):
    if request.method == 'POST':
        ticket_id = int(request.POST.get('ticket_id'))
        ticket_to_delete = Ticket.objects.get(id=ticket_id)
        ticket_to_delete.delete()
        return HttpResponseRedirect('/tickets')
        # tickets = Ticket.objects.filter(user=user)
        # return render(request, 'home/tickets.html', {'tickets': tickets})


def contactview(request):
    return render(request, 'home/contact.html')


def accountsview(request):
    return render(request, 'home/accounts.html')


# views for logging and authorization

def login_view(request):
    c = {}
    c.update(csrf(request))
    return render(request, 'home/login.html', c)


def auth_view(request):
    username = request.POST.get('username', '')  # w Django 11 piszemy  i POST WIELKi literami
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        return HttpResponseRedirect('/accounts/invalid')


def loggedin_view(request):
    return render(request, 'home/loggedin.html',
                  {"fullname": request.user.first_name})


def invalidlogin_view(request):
    return render(request, 'home/invalid_login.html')


def logout_view(request):
    logout(request)
    return render(request, 'home/logout.html')


def register_user_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)  # passing to the built-in form the information from POST
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/register_success')

    context = {}
    context.update(csrf(request))
    context['forms'] = UserCreationForm()
    return render(request, 'home/register.html', context)


def registersuccess_view(request):
    return render(request, 'home/register_success.html')


def screening_view(request):
    movie_id = request.GET.get('movie_id', default=1)
    if movie_id:
        movies = Movie.objects.filter(id=movie_id)  # queryset zeby wziac movie z tym id
        screenings = Screening.objects.filter(movie=movies)  # wyswietl screnings tego filmu
    else:
        movies = None
        screenings = Screening.objects.all()
    return render(request,
                  'home/screenings.html',
                  dict(screenings=screenings,
                       movies=movies))  # screenings i movie to dwa przesyłane contexty, czyli słownikopodobne obiekty


def vue_view(request):
    return render(request, 'home/vue.html')


def ajaxview(request):
    movies = Movie.objects.all()
    evaluations = Evaluation.objects.all()
    return render(request, 'home/ajax.html', dict(movies=movies,
                                                  evaluations=evaluations))


def evaluateview(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        opinion = request.POST.get('opinion')
        mark = request.POST.get('mark')
        title = request.POST.get('movie')
        seans = Movie.objects.get(title=title)

        Evaluation.objects.create(
            author=name,
            opinion=opinion,
            mark=mark,
            seans=seans,
        )
        return HttpResponse('')
    # od tego momentu nie działa
    else:
        response = HttpResponse()
        response['Content-Type'] = "text/javascript"
        response.write(serializers.serialize("json",
                                             Evaluation.objects.filter(pk__gt=id)))
        return response


def vue_comment_view(request):
    context = {}
    context['comments'] = Evaluation.objects.all()
    context['movies'] = Movie.objects.all()
    html = TemplateResponse(request,
                            'home/evaluationVUElist.html',
                            context)
    return HttpResponse(html.render())


class CommentViewSet(viewsets.ModelViewSet):
    # tutaj tworzony jest endpoint pozwalający wyświetlać komentarze
    queryset = Evaluation.objects.all()
    serializer_class = CommentsSerializer


def thegame_view(request):
    movies=Movie.objects.all()
    return render(request, 'home/szubienica.html',
                  {"movies": movies})