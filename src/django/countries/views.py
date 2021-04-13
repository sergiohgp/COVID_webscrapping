from django.shortcuts import render
from django.http import HttpResponse
from .models import Country, Covid_Cases


# Create your views here.
def country_list(req):
    country = Country.objects.all()

    context = {
        'country_list': country
    }

    return render(req, 'countries/country_list.html', context)
