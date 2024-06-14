from django.shortcuts import render

# Create your views here.
# convertor/views.py


def landing_page(request):
    return render(request, 'pages/home.html')

def upload_video(request):
    if request.method == 'POST':
        # Handle file upload
        pass
    return render(request, 'pages/upload.html')
