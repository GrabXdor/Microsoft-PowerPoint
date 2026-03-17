# src/animation/transition.py
class Transition:
    """Переход (эффект смены) между двумя слайдами."""

    TYPES = ["fade", "push", "wipe", "split", "morph", "none"]

    def __init__(self, trans_type: str = "fade", duration: float = 1.0):
        self.type = trans_type
        self.duration = duration

    def __str__(self):
        return f"Переход: {self.type} ({self.duration} сек)"