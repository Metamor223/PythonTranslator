from PIL import Image
import pytesseract

def ReadingText():
    # Указываем путь к установленному Tesseract OCR
    pytesseract.pytesseract.tesseract_cmd = ''

    # Открываем изображение с текстом
    image_path = 'screenGrab.png'
    img = Image.open(image_path)

    # Используем Tesseract для распознавания текста
    text = pytesseract.image_to_string(img)
    return text