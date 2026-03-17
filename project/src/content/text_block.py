# Модуль работы с текстовыми блоками
class TextBlock:
    def __init__(self, text="", font_size=18):
        self.text = text
        self.font_size = font_size
        print("Текстовый блок создан")