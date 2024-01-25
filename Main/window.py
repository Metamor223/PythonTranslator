import tkinter as tk
import mss
from PIL import Image
import pygetwindow as gw
import pygetpixel as gp

from WorkWithText.Translate import TranslateText
from WorkWithText.ReadingText import ReadingText

def ScreenGrabAndDisplay(last_text=""):
    # Получаем активное окно
    window = gw.getActiveWindow()

    if window:
        # Читаем текст из активного окна
        text = ReadingText(window)

        # Переводим текст с английского на русский
        translated_text = TranslateText(text)

        # Форматируем текст
        formatted_text = f"Text: {text}\nTranslation: {translated_text}"

    # Проверяем, добавлялся ли уже такой текст
    if formatted_text != last_text:
        # Очищаем содержимое виджета Text
        text_widget.delete("1.0", tk.END)

        # Добавляем новый текст
        text_widget.insert(tk.END, formatted_text)

    # Запускаем функцию повторно через 5000 миллисекунд (5 секунд) с новым last_text
    root.after(5000, ScreenGrabAndDisplay, formatted_text)

root = tk.Tk()
root.title("Desktop Window")

# Создаем виджет Text для отображения текста с возможностью скролла
text_widget = tk.Text(root, font=("Arial", 9), wrap=tk.WORD, width=80, height=30, padx=30, pady=30)
text_widget.pack()

# Создаем вертикальный скроллбар и привязываем его к виджету Text
scrollbar = tk.Scrollbar(root, command=text_widget.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_widget.config(yscrollcommand=scrollbar.set)

# Начинаем процесс автоматического обновления
ScreenGrabAndDisplay()

# Создаем кнопку для закрытия окна
close_button = tk.Button(root, text="Close", command=root.destroy)
close_button.pack()

# Запускаем главный цикл tkinter
root.mainloop()