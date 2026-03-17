# src/content/table.py
"""Модуль для работы с таблицами на слайдах презентации."""

class Table:
    """Таблица на слайде (матрица ячеек с возможностью заполнения).

    Attributes
    ----------
    rows : int
        Количество строк
    cols : int
        Количество столбцов
    data : list[list[str]]
        Двумерный список содержимого ячеек
    has_header : bool
        Есть ли заголовочная строка (по умолчанию True)
    """

    def __init__(self, rows: int = 3, cols: int = 4):
        """Создаёт пустую таблицу заданного размера.

        Parameters
        ----------
        rows : int, optional
            Количество строк (по умолчанию 3)
        cols : int, optional
            Количество столбцов (по умолчанию 4)
        """
        self.rows = rows
        self.cols = cols
        self.data = [["" for _ in range(cols)] for _ in range(rows)]
        self.has_header = True