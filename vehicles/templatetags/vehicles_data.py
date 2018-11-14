from django import template

register = template.Library()


@register.simple_tag
def get_distance(vehicle, date_from=None, date_to=None):
    return vehicle.distance(date_from, date_to)
