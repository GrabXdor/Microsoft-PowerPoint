# src/design/color_scheme.py
"""Модуль цветовых схем презентации."""

class ColorScheme:
    """Набор именованных цветов, используемых в теме оформления.

    Attributes
    ----------
    colors : dict
        Словарь ролей и соответствующих им HEX-цветов
    """

    def __init__(self):
        self.colors = {
            "background": "#FFFFFF",
            "text": "#000000",
            "accent1": "#0078D4",
            "accent2": "#107C41",
            "accent3": "#D83B01"
        }

    def get_color(self, role: str) -> str:
        """Получить цвет по роли.

        Parameters
        ----------
        role : str
            Название роли цвета ("background", "text", "accent1" и т.д.)

        Returns
        -------
        str
            HEX-цвет или чёрный по умолчанию
        """
        return self.colors.get(role, "#000000")