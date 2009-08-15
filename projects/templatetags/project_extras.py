from django import template

register = template.Library()

@register.filter
def isin(value,arg):
    return value in arg
    
@register.filter
def notin(value,arg):
    return value not in arg