from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def get_range(value):
    """Get a range of numbers from 0 to value-1."""
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(0) 