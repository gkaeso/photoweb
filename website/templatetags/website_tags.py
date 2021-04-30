from django import template
from django.urls import resolve


register = template.Library()


@register.simple_tag
def active_page(request, view_name):
    output: str

    if request:
        try:
            output = 'colorlib-active' if resolve(request.path_info).url_name == view_name else ''
        except Resolver404 as e:
            raise template.VariableDoesNotExist('Error setting active_page tag', e)

    return output

