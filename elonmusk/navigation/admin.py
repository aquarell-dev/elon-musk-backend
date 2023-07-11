from django.contrib import admin

from .models import NavigationLink


@admin.register(NavigationLink)
class NavigationLinkAdmin(admin.ModelAdmin):
    list_display = ['id', 'link', 'href', 'order']
    list_display_links = ['id']
    list_editable = ['order']
