from django.contrib import admin

from .models import Movie, Room, Screening, Evaluation

admin.site.register(Movie)
admin.site.register(Room)
admin.site.register(Screening)
admin.site.register(Evaluation)


