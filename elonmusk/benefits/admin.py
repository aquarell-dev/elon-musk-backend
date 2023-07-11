from django.contrib import admin

from .models import Benefit


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['id', 'preview', 'top', 'middle', 'bottom']
    list_display_links = ['id', 'preview']

    def preview(self, instance: Benefit):
        return ' '.join([instance.top, instance.middle, instance.bottom])

    preview.short_description = 'Превью'
