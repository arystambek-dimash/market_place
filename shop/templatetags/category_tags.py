from django import template

register = template.Library()


@register.inclusion_tag('./subcategories.html')
def render_subcategories(category, depth=3):
    if depth <= 0:
        return {'category': category, 'max_depth_exceeded': True}
    else:
        return {'category': category, 'max_depth_exceeded': False, 'depth': depth - 1}
