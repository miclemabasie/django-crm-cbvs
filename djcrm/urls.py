

from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from leads.views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='landing_page'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('leads/', include('leads.urls', namespace="leads")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)