from django.contrib import admin
from django.urls import path, include

from django.shortcuts import redirect

from django.conf import settings
from django.conf.urls.static import static


def redirect_to_login(request):
    return redirect('login')


urlpatterns = [

    path('', redirect_to_login),

    path('admin/', admin.site.urls),

    path('', include('movies.urls')),

    path('', include('bookings.urls')),

    path('accounts/', include('accounts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)