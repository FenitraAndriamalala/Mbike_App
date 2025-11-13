from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('velos/', include('velos.urls')),
    path('clients/', include('clients.urls')),
    path('locations/', include('locations.urls')),
    path('ammortissements/', include('ammortissements.urls')),
    path('suivi/', include('suivi.urls')),
    path('incidents/', include('incidents.urls')),
    path('anomalies/', include('anomalies.urls')),
]

# Pour servir les fichiers médias pendant le développement
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
