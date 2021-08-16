from django.shortcuts import render
from django.http import HttpResponseBadRequest

# Create your views here.
def people(req, num=0):
    
    people = [
    {
        'id': 1,
        'name': 'Bob Smith',
        'age': 35,
        'country': 'USA'
    },
    {
        'id': 2,
        'name': 'Martha Smith',
        'age': 60,
        'country': 'USA'
    },
    {
        'id': 3,
        'name': 'Fabio Alberto',
        'age': 18,
        'country': 'Italy'
    },
    {
        'id': 4,
        'name': 'Dietrich Stein',
        'age': 85,
        'country': 'Germany'
    }
    ]

    print(num)
    print(type(num))

    if num:
        person_search = [person for person in people if person['id'] == num]

        if (person_search):
            return render(req, 'people.html', {'people_list': person_search})
        else:
            return HttpResponseBadRequest('Person not found in database'.\
                                      format(req.method), status=404)
    else:
        print('no id given')
        people.sort(key = lambda person:person['age'])
        return render(req, 'people.html', {'people_list': people})