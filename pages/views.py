from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


def home_page(request):
    return render(request, 'home.html')
