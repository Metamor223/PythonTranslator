from PIL import ImageGrab, Image, ImageTk
import tkinter as tk

from Main.ReadingText import ReadingText


def screenGrabAndDisplay():
    screenGrab = ImageGrab.grab()
    screenGrab.save('Images/screenGrab.png')

    new_size = (300, 200)

    # Открываем сохраненное изображение
    original_image = Image.open('Images/screenGrab.png')

    # Изменяем размер изображения
    resized_image = original_image.resize(new_size, Image.ADAPTIVE)

    # Конвертируем изображение для Tkinter
    tk_image = ImageTk.PhotoImage(resized_image)

    # Обновляем изображение в виджете Label
    img_label.config(image=tk_image)
    img_label.image = tk_image  # Сохраняем ссылку на изображение, чтобы избежать сборщика мусора


root = tk.Tk()
root.title("Desktop Window")

img_label = tk.Label(root)  # Виджет Label для отображения изображения
img_label.pack()

text_label = ReadingText()
update_button = tk.Button(root, text="Update", command=screenGrabAndDisplay)  # Кнопка для обновления изображения
update_button.pack()

close_button = tk.Button(root, text="Close", command=root.destroy)  # Кнопка для закрытия окна
close_button.pack()

root.mainloop()
