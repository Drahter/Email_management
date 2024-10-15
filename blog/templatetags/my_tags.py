from django import template

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f'/media/blog/article_previews/{path}'
    return '#'
