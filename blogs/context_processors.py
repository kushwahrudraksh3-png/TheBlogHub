from . models import *
from about_links.models import Links


def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)


def get_links(request):
    links = Links.objects.all()
    return dict(links=links)