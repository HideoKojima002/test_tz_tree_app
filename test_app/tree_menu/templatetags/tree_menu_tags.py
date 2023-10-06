from django import template
from ..models import MenuItem


register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    try:
        menu = MenuItem.objects.get(name=menu_name)
        return build_menu_dict(menu)
    except MenuItem.DoesNotExist:
        return {}


def build_menu_dict(menu_item):
    menu_dict = {
        'name': menu_item.name,
        'url': menu_item.url,
        'children': []
    }

    children = menu_item.children.all()
    if children:
        menu_dict['children'] = [build_menu_dict(child) for child in children]

    return menu_dict


# @register.simple_tag
# def draw_menu(menu_name):
#     try:
#         menu = MenuItem.objects.get(name=menu_name)
#         return menu.children.all()  # Возвращает дочерние элементы меню
#     except MenuItem.DoesNotExist:
#         return None

# @register.simple_tag    # Рабочая страта
# def draw_menu_recursive(menu_name):
#     try:
#         menu = MenuItem.objects.get(name=menu_name)
#         return draw_menu_recursive_helper(menu)
#     except MenuItem.DoesNotExist:
#         return None
#
#
# def draw_menu_recursive_helper(menu_item):
#     if not menu_item:
#         return ""
#
#     html = f"<li><a href='{menu_item.url}'>{menu_item.name}</a>"
#
#     if menu_item.children.exists():
#         html += "<ul>"
#         for child in menu_item.children.all():
#             html += draw_menu_recursive_helper(child)
#         html += "</ul>"
#
#     html += "</li>"
#
#     return html
# @register.inclusion_tag
# @register.simple_tag
# def draw_menu(menu_name):
#     try:
#         menu = MenuItem.objects.get(name=menu_name)
#         return menu
#     except MenuItem.DoesNotExist:
#         return None


# @register.simple_tag
# def draw_menu(menu_name):
#     try:
#         menu = MenuItem.objects.get(name=menu_name)  # Изменено на menu_name
#         return menu
#     except MenuItem.DoesNotExist:
#         return None


# register = template.Library()
#


# inclusion_tag


# @register.simple_tag
# def draw_menu(menu_name):
#     menu = MenuItem.objects.filter(parent=None, menu_name=menu_name)
#     return {'menu': menu}
