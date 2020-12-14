
from django.template import Variable, VariableDoesNotExist
from django import template

register = template.Library()


@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')


@register.filter
def getattr(object, attr):
    """Create attribute to object"""
    pseudo_context = {'object': object}
    try:
        value = Variable('object.%s' % attr).resolve(pseudo_context)
    except VariableDoesNotExist:
        value = None
    return value
