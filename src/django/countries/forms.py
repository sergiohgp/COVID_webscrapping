from django import forms


class CountryForm(forms.Form):
    id = forms.CharField()
    name = forms.CharField(max_length=255)
    population = forms.IntegerField()
    flag = forms.CharField()
    area = forms.FloatField()
    total_cases = forms.IntegerField()
    new_cases = forms.IntegerField()
    total_deaths = forms.IntegerField()
