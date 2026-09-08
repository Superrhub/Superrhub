from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve as static_serve
import os

def serve_sw(request):
    from django.http import FileResponse
    sw_path = os.path.join(settings.BASE_DIR, 'static', 'sw.js')
    return FileResponse(open(sw_path, 'rb'), content_type='application/javascript')

urlpatterns = [
    path('', include('apps.stories.urls')),
    path('auth/', include('apps.users.urls')),
    path('interactions/', include('apps.interactions.urls')),
    path('sw.js', serve_sw, name='service_worker'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
