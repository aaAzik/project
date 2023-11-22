from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from drf_spectacular.views import (
    SpectacularAPIView, SpectacularSwaggerView
)

urlpatterns = [
    path('azik/', admin.site.urls),
    path('', include('scoop.urls')),
    path('account/', include('account.urls')),
    path('api/schema/', SpectacularAPIView.as_view(), name="schema"),
    path('api/schema/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)