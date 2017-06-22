import random

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.models import User

from .models import *


def homeview(request):
    return render(request, 'home/home.html')


def moviesview(request):
    movies = Movie.objects.all()
    return render(request, 'home/movies.html', {'movies': movies})


def ticketsview(request):
    user = User.objects.get(id=request.user.id)
    if request.method == 'GET':
        # name = request.GET.get('username')  # jak to zmienić na current user?
        tickets = Ticket.objects.filter(user=user)  # jak to zmienić na current user?
        return render(request, 'home/tickets.html', {'tickets': tickets})
    elif request.method == 'POST':
        screening_id = int(request.POST.get('screening_id'))
        # user_id = int(request.POST.get('user_id'))
        how_many = int(request.POST.get('how_many'))
        screening = Screening.objects.get(id=screening_id)
        # user = User.objects.get(id=user_id)
        for _ in range(how_many):
            seat = random.randint(1, 100)
            Ticket(screening=screening, user=user, seat=str(seat)).save()
        return HttpResponseRedirect(reverse('reservations:tickets'))
        # return HttpResponseRedirect('/coupons')


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
    movie_id = request.GET.get('movie_id',
                               default=1)  # bierze movie id z requesta a defacto z adresu url request.GET jest słownikiem
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
