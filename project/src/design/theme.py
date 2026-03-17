# src/design/theme.py
"""Модуль описания тем оформления презентации."""

class Theme:
    """Тема оформления слайдов (набор цветов, шрифтов, стилей).

    Attributes
    ----------
    name : str
        Название темы
    primary_color : str
        Основной цвет (HEX)
    accent_color : str
        Акцентный цвет (HEX)
    font_family : str
        Семейство шрифтов
    background_color : str
        Цвет фона по умолчанию
    """

    def __init__(self, name: str = "Default"):
        """Создаёт новую тему оформления.

        Parameters
        ----------
        name : str, optional
            Название темы (по умолчанию "Default")
        """
        self.name = name
        self.primary_color = "#0078D4"
        self.accent_color = "#FF8C00"
        self.font_family = "Calibri"
        self.background_color = "#FFFFFF"

    def __str__(self):
        return f"Тема: {self.name}"