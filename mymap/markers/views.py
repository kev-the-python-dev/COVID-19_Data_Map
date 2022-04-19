from django.shortcuts import render
from mymap.settings import MAPBOX_TOKEN
from django.http import HttpResponse
from markers.models import Marker
def index(request):
    context = {
            'MAPBOX_TOKEN':MAPBOX_TOKEN
            }
    return render(request, 'map.html', context)

