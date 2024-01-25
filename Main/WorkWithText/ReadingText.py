from PIL import Image
import pytesseract

def ReadingText(window):
    # Получаем размеры окна
    left, top, right, bottom = window.left, window.top, window.right, window.bottom

    # Захватываем содержимое окна
    screen_image = Image.frombytes('RGB', (right - left, bottom - top),
                                   gp.screenshot(region=(left, top, right, bottom)).tobytes())

    # Используем Tesseract для распознавания текста
    text = pytesseract.image_to_string(screen_image)
    return text
