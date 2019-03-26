from django.http import HttpResponse
from django.shortcuts import render
import json
import populartimes

def render_map(request):
    return render(request, 'places/map_template.html')

def render_place(request, placeID):
    return render(request, 'places/places_template.html', context={"placeID": placeID})

def get_id(request,place_id ):
    temp = populartimes.get_id("AIzaSyDkB11aWorrg7xpxVGnxHtglcyvMZbAODI", place_id)
    resp = json.dumps(temp)
    return HttpResponse(resp)