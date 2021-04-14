from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Country, Covid_Cases
import pymongo

from .forms import CountryForm

# Connect to MongoDb
client = pymongo.MongoClient('mongodb://localhost:27017/')
if client:
    DB = client['termproject']

# Create your views here.


def country_list(req):
    country = Country.objects.all()
    covid_cases = Covid_Cases.objects.all()

    country_list = []

    for i in country:
        for j in covid_cases:
            if (i.id == j.id):
                country_list.append({
                    'id': i.id,
                    'name': i.name,
                    'flag': i.flag,
                    'area': i.area,
                    'population': i.population,
                    'total_cases': j.total_cases,
                    'cases_milion': str(round((float(1000000) * float(str(j.total_cases).replace(',', '')))/float(str(i.population).replace(',', '')), 2)),
                    'new_cases': j.new_cases,
                    'total_deaths': j.total_deaths,
                })

    context = {
        'country_list': country_list
    }

    return render(req, 'countries/country_list.html', context)


def country_edit(req, id):
    country = Country.objects.get(id=id)
    covid_cases = Covid_Cases.objects.get(id=id)

    selected_country = {
        'id': id,
        'name': country.name,
        'flag': country.flag,
        'area': country.area,
        'population': country.population,
        'total_cases': str(covid_cases.total_cases).replace(',', ''),
        'new_cases': str(covid_cases.new_cases).replace(',', ''),
        'total_deaths': str(covid_cases.total_deaths).replace(',', ''),
    }

    context = {
        'country': selected_country,
    }

    return render(req, 'countries/edit_country.html', context)


def country_add(req):
    return render(req, 'countries/add_country.html')


def country_insert(req):
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            population = form.cleaned_data['population']
            area = form.cleaned_data['area']
            flag = form.cleaned_data['flag']

            total_cases = form.cleaned_data['total_cases']
            new_cases = form.cleaned_data['new_cases']
            total_deaths = form.cleaned_data['total_deaths']

            country_document = {
                'id': name + "_" + id,
                'name': name,
                'population': population,
                'area': area,
                'flag': flag
            }
            covid_cases_document = {
                'id': name + "_" + id,
                'country_name': name,
                'total_cases': total_cases,
                'new_cases': new_cases,
                'total_deaths': total_deaths,
            }

            col = DB['countries_country']
            if col:
                document_exists = col.find_one({'id': id})
                if document_exists:
                    col.delete_one({'id': id})

                col.update_one(country_document, {
                               '$set': country_document}, upsert=True)

            col = DB['countries_covid_cases']
            if col:
                document_exists = col.find_one({'id': id})
                if document_exists:
                    col.delete_one({'id': id})

                col.update_one(covid_cases_document, {
                               '$set': covid_cases_document}, upsert=True)

            return HttpResponseRedirect('/')
    else:
        form = CountryForm()

    return render(req, 'countries/add_country.html', {'form': form})


def country_update(req):
    if req.method == 'POST':
        form = CountryForm(req.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            name = form.cleaned_data['name']
            population = form.cleaned_data['population']
            area = form.cleaned_data['area']
            flag = form.cleaned_data['flag']

            total_cases = form.cleaned_data['total_cases']
            new_cases = form.cleaned_data['new_cases']
            total_deaths = form.cleaned_data['total_deaths']

            # Update into DB
            country_document = {
                'id': id,
                'name': name,
                'population': population,
                'area': area,
                'flag': flag
            }
            covid_cases_document = {
                'id': id,
                'country_name': name,
                'total_cases': total_cases,
                'new_cases': new_cases,
                'total_deaths': total_deaths,
            }

            col = DB['countries_country']
            if col:
                document_exists = col.find_one({'id': id})
                if document_exists:
                    col.delete_one({'id': id})

                col.update_one(country_document, {
                               '$set': country_document}, upsert=True)

            col = DB['countries_covid_cases']
            if col:
                document_exists = col.find_one({'id': id})
                if document_exists:
                    col.delete_one({'id': id})

                col.update_one(covid_cases_document, {
                               '$set': covid_cases_document}, upsert=True)

            return HttpResponseRedirect('/')
    else:
        form = CountryForm()

    return render(req, 'countries/edit_country.html', {'form': form})


def country_delete(req, id):
    col = DB['countries_country']
    if col:
        document_exists = col.find_one({'id': id})
        if document_exists:
            col.delete_one({'id': id})

    col = DB['countries_covid_cases']
    if col:
        document_exists = col.find_one({'id': id})
        if document_exists:
            col.delete_one({'id': id})

    return HttpResponseRedirect('/')
