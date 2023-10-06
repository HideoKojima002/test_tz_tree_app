from django.contrib import admin
from .models import MenuItem
# from django import forms

# admin.site.register(MenuItem)


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'url']
    list_filter = ['name']


admin.site.register(MenuItem, MenuItemAdmin)

# admin.site.register(MenuItem)


# class MenuItemForm(forms.ModelForm):
#     class Meta:
#         model = MenuItem
#         fields = ['title', 'parent', 'url']
#
#
# class MenuItemAdmin(admin.ModelAdmin):
#     form = MenuItemForm
#
#
# admin.site.register(MenuItem, MenuItemAdmin)