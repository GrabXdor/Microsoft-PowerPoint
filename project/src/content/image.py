# src/content/image.py
class Image:
    """Элемент изображения на слайде."""

    def __init__(self, path: str = "", width: int = 400, height: int = 300):
        """Инициализация изображения.

        Parameters
        ----------
        path : str
            Путь к файлу изображения
        width, height : int
            Желаемые размеры отображения
        """
        self.path = path
        self.width = width
        self.height = height
        self.alt_text = ""

    def __str__(self):
        return f"Изображение: {self.path} ({self.width}×{self.height})"