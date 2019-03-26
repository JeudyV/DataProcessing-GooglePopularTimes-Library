import populartimes
from django import template


register = template.Library()

@register.simple_tag()
def get_id(place_id ):
    return populartimes.get_id("AIzaSyDkB11aWorrg7xpxVGnxHtglcyvMZbAODI", place_id)
