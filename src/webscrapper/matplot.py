import matplotlib.pyplot as plt
import numpy as np
import pymongo


client = pymongo.MongoClient('mongodb://localhost:27017')
if client:
    DB = client['termproject']


def showPlot():
    col = DB.get_collection('countries_covid_cases')
    if col:
        CAD = col.find_one({'country_name': 'Canada'})
        BRA = col.find_one({'country_name': 'Brazil'})
        USA = col.find_one({'country_name': 'United States'})

    n_groups = 3

    total_cases = (int(str(CAD['total_cases']).replace(",", ""))/1000000, int(str(
        BRA['total_cases']).replace(",", ""))/1000000, int(str(USA['total_cases']).replace(",", ""))/1000000)

    total_deaths = (int(str(CAD['total_deaths']).replace(',', ''))/100000, int(str(
        BRA['total_deaths']).replace(',', ''))/100000, int(str(USA['total_deaths']).replace(',', ''))/100000)

    fig, ax = plt.subplots()

    index = np.arange(n_groups)
    bar_width = 0.35

    opacity = 0.4
    error_config = {'ecolor': '0.3'}

    rects1 = plt.bar(index, total_cases, bar_width,
                     alpha=opacity,
                     color='b',
                     error_kw=error_config,
                     label='Total Cases/Milion')

    rects2 = plt.bar(index + bar_width, total_deaths, bar_width,
                     alpha=opacity,
                     color='r',
                     error_kw=error_config,
                     label='Total Deaths/100 Thousand')

    plt.ylabel('Covid Cases Numbers')
    plt.title('Covid Cases by country')
    plt.xticks(index + bar_width / 2, ('Canada', 'Brazil', 'USA'))

    plt.legend()
    plt.tight_layout()
    plt.show()


showPlot()
