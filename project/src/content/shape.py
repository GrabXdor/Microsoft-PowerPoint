# Фигуры (прямоугольник, круг, стрелка и т.д.)

class Shape:
    TYPES = ["rectangle", "circle", "arrow", "star", "line"]

    def __init__(self, shape_type: str = "rectangle", color: str = "#4682B4"):
        self.shape_type = shape_type
        self.color = color
        self.x = 0
        self.y = 0
        self.width = 200
        self.height = 100

    def __str__(self):
        return f"Фигура {self.shape_type} цвета {self.color}"