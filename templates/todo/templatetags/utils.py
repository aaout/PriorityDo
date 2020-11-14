from django import template

register = template.Library()

@register.filter(name="sum")
def sum(arg1, arg2,arg3):
    return arg1 + arg2 + arg3
