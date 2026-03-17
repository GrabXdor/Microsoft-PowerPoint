# Точка входа в приложение презентаций

from slides.slide import Slide
from content.text_block import TextBlock
from design.theme import Theme

def main():
    print("Запуск программы презентаций...")

    # Пример создания презентации
    slide = Slide()
    slide.add_element(TextBlock("Добро пожаловать в презентацию!", font_size=44))
    
    theme = Theme(name="Corporate Blue")
    slide.apply_theme(theme)
    
    print("Слайд создан и оформлен.")

if __name__ == "__main__":
    main()