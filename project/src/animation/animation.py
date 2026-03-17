# src/animation/animation.py
class Animation:
    """Анимация, применяемая к элементу слайда."""

    TYPES = ["appear", "fade", "fly_in", "zoom", "spin"]

    def __init__(self, anim_type: str = "appear", duration: float = 1.0):
        """Создание анимации для элемента.

        Parameters
        ----------
        anim_type : str
            Тип анимации (из Animation.TYPES)
        duration : float
            Продолжительность в секундах
        """
        self.type = anim_type
        self.duration = duration
        self.delay = 0.0
        self.target_element = None

    def apply_to(self, element):
        """Привязать анимацию к конкретному объекту на слайде."""
        self.target_element = element
        print(f"Анимация '{self.type}' применена")