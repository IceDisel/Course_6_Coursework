from django import template
from django.contrib.auth.models import Group

register = template.Library()


@register.filter()
def my_media(data):
    if data:
        return f'/media/{data}'
    return '#'


@register.filter()
def first_three_words(string):
    words = string.split()
    three_words = " ".join(words[:3])
    return three_words


@register.filter
def in_group(user, group_name):
    group = Group.objects.get(name=group_name)
    return group in user.groups.all()
