import time
import pyautogui
import keyboard

click_count = 500

def close_script(e):
    if e.name == 'left windows' or e.name == 'right windows':
        global running
        running = False

keyboard.on_press(close_script)

running = True

for _ in range(click_count):
    if not running:
        break
    pyautogui.click()
    time.sleep(0.3)

keyboard.unhook_all()  # Отключаем обработчик нажатий клавиш перед выходом

#version 2.0

# import tkinter as tk
# import time
# import pyautogui
# import threading
# import keyboard

# click_count = 15
# running = False

# def run_app():
#     global running
#     running = True
#     for _ in range(click_count):
#         if not running:
#             break
#         pyautogui.click()
#         time.sleep(2)
#     change_button_color('red')

# def stop_app():
#     global running
#     running = False
#     change_button_color('green')

# def change_button_color(color):
#     start_button.config(bg=color)

# def close_script(e):
#     if e.event_type == keyboard.KEY_DOWN and (e.name == 'f9' or e.name == 'f8'):
#         if e.name == 'f9':
#             run_app()
#         elif e.name == 'f8':
#             stop_app()

# # Создаем окно
# window = tk.Tk()
# window.title("Управление приложением")

# # Создаем кнопку "Запустить"
# start_button = tk.Button(window, text="Запустить", command=run_app, bg="green")
# start_button.pack()

# # Создаем кнопку "Остановить"
# stop_button = tk.Button(window, text="Остановить", command=stop_app, bg="red")
# stop_button.pack()

# # Добавляем обработчик клавиш
# keyboard.hook(close_script)

# # Запускаем интерфейс
# window.mainloop()

# # Отключаем обработчик нажатий клавиш перед выходом
# keyboard.unhook_all()
