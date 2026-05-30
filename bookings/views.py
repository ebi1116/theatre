from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Movie, Show, Booking


def seat_selection(request, movie_id, show_id):

    movie = Movie.objects.get(id=movie_id)
    show = Show.objects.get(id=show_id)

    rows = ['A', 'B', 'C', 'D', 'E']
    cols = ['1', '2', '3', '4', '5', '6', '7', '8']

    booked_seats = Booking.objects.filter(
        show=show
    ).values_list('seat_number', flat=True)

    if request.method == 'POST':

        selected_seats = request.POST.getlist('selected_seats')

        for seat in selected_seats:

            Booking.objects.create(
                user=request.user,
                movie=movie,
                show=show,
                seat_number=",".join(selected_seats)
            )
        return render(request, 'booking_sucess.html', {
            'selected_seats': selected_seats
        })

    context = {
        'movie': movie,
        'show': show,
        'rows': rows,
        'cols': cols,
        'booked_seats': booked_seats
    }

    return render(request, 'seat_selection.html', context)