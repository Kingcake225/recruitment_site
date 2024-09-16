from django.shortcuts import render
from django.http import HttpResponse

def route(request):
    context = {
        'title': 'Loose Change - Best Route',
    }
    return render(request, 'distanceToOffice/route.html', context)