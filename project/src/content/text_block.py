# src/content/text_block.py
"""Текстовые блоки / надписи / заголовки / абзацы."""

class TextBlock:
    """Элемент текста на слайде (надпись, заголовок, абзац).

    Attributes
    ----------
    text : str
        Содержимое текстового блока
    font_size : int
        Размер шрифта в пунктах
    color : str
        Цвет текста в формате HEX
    bold : bool
        Полужирное начертание
    italic : bool
        Курсив
    """

    def __init__(self, text: str = "", font_size: int = 18, color: str = "#000000"):
        self.text = text
        self.font_size = font_size
        self.color = color
        self.bold = False
        self.italic = False

    def __str__(self):
        return f"Текст: '{self.text}' (размер {self.font_size}, цвет {self.color})"

    def set_bold(self, bold: bool = True):
        """Включить или выключить полужирное начертание."""
        self.bold = bold