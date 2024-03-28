import cv2
import numpy as np

# Функция для создания видео с бегущей строкой
def create_running_line(text="Hello, world!"):

    message = text + '  ' # Пробелы для полного прокурчивания строки
    
    width, height = 512, 512    # Размеры видео (ширина x высота)
    duration = 3                # Длительность видео (секунды)
    fps = 24                    # Кадры в секунду

    # Задаём параметры - видеопоток с частотой fps
    out = cv2.VideoWriter('.//videoCreator//creator//videos//' + text + ".mp4", cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

    # Создаем кадр с черным фоном
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    # Начальные координаты для бегущей строки
    x, y = width, height - height // 4

    # Установим параметры шрифта
    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 15
    font_thickness = 10
    font_color = (255, 255, 255)  # Белый цвет текста

    text_width, text_height = cv2.getTextSize(message, font, font_scale, font_thickness)[0]
    # Пройдемся по каждому кадру
    for _ in range( duration * fps ):
        # Очистка кадра
        frame.fill(0)

        # Новые координаты для бегущей строки
        x -= text_width //(fps * duration)  # Скорость бегущей строки

        # Вот тут добавим текст
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)

        # Тут запишем кадр
        out.write(frame)

    # Закроем тут видеопоток
    out.release()
