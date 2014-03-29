from django import template
register = template.Library()

# Return "active" if the pattern is in the URL path
@register.simple_tag
def active(request, pattern):
    import re
    if pattern == "/" and request.path == "/":
        return 'active'
    elif pattern != "/" and re.search(pattern, request.path):
        return 'active'
    return ''
