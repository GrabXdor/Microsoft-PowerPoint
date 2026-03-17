# src/slides/slide.py
"""Модуль, содержащий основной класс Slide — представление одного слайда презентации."""

from content.text_block import TextBlock
from content.image import Image
from design.theme import Theme


class Slide:
    """Класс, представляющий один слайд презентации.

    Attributes
    ----------
    layout : str
        Тип макета слайда (по умолчанию "title_and_content")
    elements : list
        Список объектов-контента на слайде
    background : Background or None
        Фон слайда
    theme : Theme or None
        Применённая тема оформления
    """

    def __init__(self, layout="title_and_content"):
        self.layout = layout
        self.elements = []
        self.background = None
        self.theme = None

    def add_element(self, element):
        """Добавить элемент контента на слайд.

        Parameters
        ----------
        element : TextBlock | Image | Shape | Table | ...
            Объект, реализующий __str__ или имеющий метод отображения
        """
        self.elements.append(element)

    def apply_theme(self, theme: Theme):
        """Применить тему оформления к слайду.

        Parameters
        ----------
        theme : Theme
            Объект темы, содержащий цвета, шрифты и т.д.
        """
        self.theme = theme
        print(f"Применена тема: {theme.name}")

    def set_background(self, background):
        """Установить фон слайда.

        Parameters
        ----------
        background : Background
            Объект фона (сплошной цвет, градиент, изображение и т.д.)
        """
        self.background = background

    def render(self):
        """Вывести в консоль текстовое представление слайда (для отладки)."""
        print(f"Слайд (макет: {self.layout})")
        for el in self.elements:
            print(f"  - {el}")