from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from pages.views import home_page



#work on this urlpatterns
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", include("pages.urls")),
    path('', home_page, name='landing'),
    path('convert/', include('convertor.urls'))
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
