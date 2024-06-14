from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
 

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    path('admin/', admin.site.urls),
    path('', include('convertor.urls')),  # Include convertor app URLs
    path('about/', TemplateView.as_view(template_name='pages/about.html'), name='about'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
