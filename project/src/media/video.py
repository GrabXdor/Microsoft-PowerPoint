# src/media/video.py
"""Модуль для вставки видео на слайды."""

class Video:
    """Видеофайл, встраиваемый в слайд.

    Attributes
    ----------
    path : str
        Путь к видеофайлу
    width : int
        Ширина отображения
    height : int
        Высота отображения
    autoplay : bool
        Автоматическое воспроизведение
    controls : bool
        Показывать элементы управления
    """

    def __init__(self, path: str = "", width: int = 640, height: int = 360):
        """Инициализация видео-элемента.

        Parameters
        ----------
        path : str, optional
            Путь к файлу
        width : int, optional
            Ширина в пикселях
        height : int, optional
            Высота в пикселях
        """
        self.path = path
        self.width = width
        self.height = height
        self.autoplay = False
        self.controls = True