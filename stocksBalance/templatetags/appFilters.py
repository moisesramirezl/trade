from django import template
import pandas as pd


register = template.Library()


@register.filter(name='getItem')
def getItem(dictionary, key):
    return dictionary.get(key)


@register.filter()
def toInt(value):
    return int(value)


@register.filter()
def toFloat(value):
    print(value)
    value = value.replace('.', '')
    floatValue = float(value.replace(',', '.'))
    return floatValue
