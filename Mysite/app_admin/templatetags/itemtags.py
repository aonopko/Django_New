from django import template

from django.shortcuts import render

from ..models import Item

register = template.Library()

@register.simple_tag()
def get_item():
    return Item.name
