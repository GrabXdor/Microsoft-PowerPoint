# src/media/audio.py
"""Модуль для вставки аудио на слайды."""

class Audio:
    """Аудиофайл, встраиваемый в слайд.

    Attributes
    ----------
    path : str
        Путь к аудиофайлу
    autoplay : bool
        Автоматическое воспроизведение при показе слайда
    loop : bool
        Зацикленное воспроизведение
    volume : float
        Уровень громкости (0.0–1.0)
    """

    def __init__(self, path: str = "", autoplay: bool = False, loop: bool = False):
        """Инициализация аудио-элемента.

        Parameters
        ----------
        path : str, optional
            Путь к файлу
        autoplay : bool, optional
            Автозапуск
        loop : bool, optional
            Зацикливание
        """
        self.path = path
        self.autoplay = autoplay
        self.loop = loop
        self.volume = 1.0