from django.urls import path
from .views import upload_video, landing_page

urlpatterns = [
    path('upload/', upload_video, name='upload_video'),
    path('', landing_page, name='landing_page'),
]
