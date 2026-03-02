from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    """MVP модель для слайдера"""

    pic = FilerImageField(verbose_name='Изображение', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(verbose_name='Пометка', max_length=100)
    order = models.PositiveIntegerField(verbose_name='Порядок', default=0)

    class Meta:
        verbose_name = 'Слайды'
        verbose_name_plural = 'Слайд'
        ordering = ['order']

    def __str__(self):
        return self.title
