from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = (
        'movie',
        'show',
        'seat_number',
        'booked_at'
    )