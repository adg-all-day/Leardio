from django.shortcuts import render
from django.http import HttpResponse

def landing_page(request):
    return render(request, 'pages/landing.html')

def upload_video(request):
    if request.method == 'POST':
        # Handle file upload
        pass
    return render(request, 'pages/upload.html')
