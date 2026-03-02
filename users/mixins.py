class WhiteMontserratMixin:
    """
    Миксин для формы:
    - цвет текста белый
    - placeholder черный
    - шрифт Montserrat
    """

    BASE_STYLE = (
        "font-family: 'Montserrat', -apple-system, 'Segoe UI', sans-serif;"
        "color: black;"
    )

    def apply_style(self, field):
        """Применяет стили к полю формы"""
        attrs = field.widget.attrs

        existing_style = attrs.get('style', '')
        attrs['style'] = existing_style + self.BASE_STYLE if existing_style else self.BASE_STYLE

        attrs.setdefault('placeholder', field.label or '')
        attrs.setdefault('class', 'form-control')

        return field

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            self.apply_style(field)
            field.label = ''
            field.help_text = ''
