import pathlib
from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    my_title = "My Page"
    my_context = {
        "page_title": my_title,
        "qs": qs.count(),
    }
    html_template = "home.html"
    PageVisit.objects.create()
    return render(request, html_template, my_context)
