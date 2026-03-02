from django.views.generic import TemplateView
from .models import Slider


class MainPageView(TemplateView):
    """View для main_page"""

    template_name = 'web_app/main_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все слайды с изображениями, сортируем по order
        slides = Slider.objects.filter(pic__isnull=False).order_by('order')

        context['slides'] = slides
        context['first_slide'] = slides.first() if slides.exists() else None
        context['has_slides'] = slides.exists()

        return context
