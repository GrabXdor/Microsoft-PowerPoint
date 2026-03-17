# src/slides/master_slide.py
"""Мастер-слайд — глобальный шаблон оформления для всех слайдов презентации."""

class MasterSlide:
    """Шаблон (мастер-слайд), определяющий настройки по умолчанию для всей презентации."""

    def __init__(self):
        self.default_theme = None
        self.default_background = None
        self.placeholders = {}

    def set_default_theme(self, theme):
        """Установить тему, которая будет применяться ко всем новым слайдам по умолчанию."""
        self.default_theme = theme

    def apply_to_slide(self, slide):
        """Применить настройки мастер-слайда к конкретному слайду."""
        if self.default_theme:
            slide.apply_theme(self.default_theme)
        # Здесь можно применять другие глобальные настройки