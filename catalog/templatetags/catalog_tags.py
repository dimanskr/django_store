import datetime
from django import template

register = template.Library()


# Тег текущего времени
@register.simple_tag
def current_time(format_string='%Y'):
    return datetime.datetime.now().strftime(format_string)


# фильтр вывода полного пути к изображению
@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"
