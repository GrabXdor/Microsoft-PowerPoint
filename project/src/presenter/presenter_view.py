# src/presenter/presenter_view.py
class PresenterView:
    """Режим представления для докладчика (заметки, таймер, текущий слайд)."""

    def __init__(self):
        self.current_slide_index = 0
        self.notes = ""
        self.timer_running = False

    def show_notes(self):
        """Вывести заметки докладчика для текущего слайда."""
        print("Заметки докладчика:", self.notes)

    def start_timer(self):
        """Запустить таймер презентации."""
        self.timer_running = True
        print("Таймер презентации запущен")