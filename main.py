from tkinter import Tk
from tkinter.filedialog import askopenfilename
import video_trimmer

# Открываем диалоговое окно для выбора файла mp4
Tk().withdraw()
filename = askopenfilename(title="Выберите файл mp4")

# Проверяем, был ли выбран файл
if not filename:
    print("Файл не выбран.")
    exit()

# Запрос пользовательского ввода начального и конечного времени обрезки (в секундах)
start_time = float(input("Введите начальное время обрезки (в секундах): "))
end_time = float(input("Введите конечное время обрезки (в секундах): "))

# Вызываем функцию обрезки видео из другого файла
output_filename = video_trimmer.trim_video(filename, start_time, end_time)

print("Обрезка завершена. Результат сохранен в файле:", output_filename)