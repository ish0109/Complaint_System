from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # login/logout
    path('', include('complaints.urls')),  # complaints app
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)