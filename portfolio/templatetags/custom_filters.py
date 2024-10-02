from django import template

register = template.Library()

@register.filter(name='split')
def split(value, delimiter):
    """Splits the value by the given delimiter."""
    if not isinstance(value, str):
        return value
    return value.split(delimiter)
