# src/design/background.py
"""Модуль описания фонов слайдов."""

class Background:
    """Фон слайда (сплошной цвет, градиент, изображение, узор).

    Attributes
    ----------
    type : str
        Тип фона ("solid", "gradient", "picture", "pattern")
    color : str
        Основной цвет (для solid и начала градиента)
    image_path : str or None
        Путь к фоновому изображению (если type == "picture")
    gradient_start : str or None
        Начальный цвет градиента
    gradient_end : str or None
        Конечный цвет градиента
    """

    TYPES = ["solid", "gradient", "picture", "pattern"]

    def __init__(self, bg_type: str = "solid", color: str = "#FFFFFF"):
        """Инициализация фона.

        Parameters
        ----------
        bg_type : str, optional
            Тип фона (по умолчанию "solid")
        color : str, optional
            Основной цвет (по умолчанию белый)
        """
        self.type = bg_type
        self.color = color
        self.image_path = None
        self.gradient_start = None
        self.gradient_end = None