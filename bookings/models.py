from django.db import models
from django.contrib.auth.models import User
from movies.models import Movie, Show


class Booking(models.Model):

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE)
    seat_number = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        default=""
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.movie} - {self.seat_number}"