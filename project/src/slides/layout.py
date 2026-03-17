# src/slides/layout.py
"""Константы и валидация макетов слайдов."""

class Layout:
    """Перечисление поддерживаемых типов макетов слайдов."""

    TYPES = [
        "title_slide",
        "title_and_content",
        "two_content",
        "picture_with_caption",
        "blank",
    ]

    @staticmethod
    def validate(layout_name: str) -> bool:
        """Проверить, является ли переданное имя макета допустимым.

        Returns
        -------
        bool
            True если макет существует в списке TYPES
        """
        return layout_name in Layout.TYPES