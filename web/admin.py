from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.html import format_html

from .models import Slider


@admin.register(Slider)
class SliderAdmin(SortableAdminMixin, admin.ModelAdmin):
    """Админка для слайдера"""

    list_display = ('preview', 'title',)
    search_fields = ('title',)

    def preview(self, obj):
        if obj.pic:
            return format_html('<img src="{}" style="height: 60px;" />', obj.pic.url)
        return "—"

    preview.short_description = "Превью"
