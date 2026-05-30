from django.urls import path
from .views import seat_selection

urlpatterns = [
    path(
        'seats/<int:movie_id>/<int:show_id>/',
        seat_selection,
        name='seat_selection'
    ),
]