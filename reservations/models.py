from django.contrib.auth.models import User
from django.db import models
from django.contrib import admin
from django.db.models import permalink


class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=150)
    description = models.TextField(default="Opis")
    date = models.IntegerField(default=2000)
    genre = models.CharField(max_length=100, default="Thriller")
    poster_url = models.CharField(max_length=500)

    class Meta:
        verbose_name_plural = "movies"

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "rooms"

    def __str__(self):
        return str(self.number)


class Screening(models.Model):
    DAY_STATUS = ((0, 'Monday'),
                  (1, 'Tuesday'),
                  (2, 'Wednesday'),
                  (3, 'Thursday'),
                  (4, 'Friday'),
                  (5, 'Saturday'),
                  (6, 'Sunday'))

    HOUR_STATUS = ((0, '8:00'),
                   (1, '8:30'),
                   (2, '9:00'),
                   (3, '9:30'),
                   (4, '10:00'),
                   (5, '10:30'),
                   (6, '11:00'),
                   (7, '11:30'),
                   (8, '12:00'),
                   (9, '12:30'),
                   (10, '13:00'),
                   (11, '13:30'),
                   (12, '14:00'),
                   (13, '14:30'),
                   (14, '15:00'),
                   (15, '15:30'),
                   (16, '16:00'),
                   (17, '16:30'),
                   (18, '17:00'),
                   (19, '17:30'),
                   (20, '18:00'),
                   (21, '18:30'),
                   (22, '19:00'),
                   (23, '19:30'),
                   (24, '20:00'),
                   (25, '20:30'))

    movie = models.ForeignKey(Movie)
    room_nr = models.ForeignKey(Room)
    view_day = models.IntegerField(default=0, choices=DAY_STATUS)
    view_hour = models.IntegerField(default=0, choices=HOUR_STATUS)

    class Meta:
        verbose_name_plural = "screenings"

    def __str__(self):
        day = self.get_view_day_display()
        hour = self.get_view_hour_display()
        return str(day) + "\t" + str(hour) + "\t" + str(self.movie)

class Ticket(models.Model):
    screening = models.ForeignKey(Screening)
    user = models.ForeignKey(User)
    seat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "tickets"

    def __str__(self):
        return str(self.screening) + str(self.user)


class Evaluation(models.Model):
    MARK_CHOICES = (
        (1, "*"),
        (2, "**"),
        (3, "***"),
        (4, "****"),
        (5, "*****"),
        (6, "******"),
    )
    opinion = models.TextField(max_length=1000)
    seans = models.ForeignKey(Movie, default=1)
    author = models.TextField(max_length=100, default="Anonymous")
    mark = models.IntegerField(choices=MARK_CHOICES, default=6)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "evaluations"
        ordering = ('-timestamp',)

    def __str__(self):
        return "Opinion by " + str(self.author) + " from " + str(self.timestamp)

    @permalink
    def get_absolute_url(self):
        return ('django.views.generic.list_detail.object_detail', None, {'object_id': self.id})

    class EvaluationAdmin(admin.ModelAdmin):
        list_display = ('__str__', 'text', 'mark', 'seans')
        list_filter = ('timestamp', 'author')
