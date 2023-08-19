import time
import pyautogui
import keyboard

click_count = 15

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
    time.sleep(2)

keyboard.unhook_all()  # Отключаем обработчик нажатий клавиш перед выходом
