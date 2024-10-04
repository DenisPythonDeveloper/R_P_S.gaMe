import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# Возможные варианты выбора
choices = ["R", "P", "S"]
image_path = os.path.join(os.path.dirname(__file__), "image")

def start_carousel():
    global carousel_id
    if running:
        # Выбираем случайный вариант для компьютера
        computer_choice = random.choice(choices)
        update_computer_image(computer_choice)
        
        # Запускаем карусель с задержкой
        carousel_id = root.after(int(carousel_speed * 100), start_carousel)  # задержка в миллисекундах

def stop_carousel():
    global carousel_id
    # Останавливаем карусель
    if carousel_id is not None:
        root.after_cancel(carousel_id)
        carousel_id = None

def update_computer_image(choice):
    img = images[choice]
    computer_label.config(image=img)

def update_user_image(choice):
    img = images[choice]
    user_label.config(image=img)

def stop_game():
    global running
    stop_carousel()  # Останавливаем карусель
    result = check_winner(user_choice, computer_choice)
    result_label.config(text=result)
    running = False  # Останавливаем игру

def check_winner(user, computer):
    if user == computer:
        return "Tie!"
    elif (user == "R" and computer == "S") or \
         (user == "S" and computer == "P") or \
         (user == "P" and computer == "R"):
        return "Amazing! You win!"
    else:
        return "Oh! Computer wins!"

def on_user_choice(choice):
    global user_choice, running, computer_choice
    user_choice = choice
    update_user_image(user_choice)

    # Останавливаем игру и карусель, если она уже запущена
    if running:
        stop_carousel()
    
    # Запускаем карусель
    running = True
    computer_choice = random.choice(choices)  # Выбираем начальное значение для компьютера
    start_carousel()
    
    # Останавливаем игру через 2 секунды (пример)
    root.after(2000, stop_game)

def set_carousel_speed(value):
    global carousel_speed
    carousel_speed = float(value)

# Главное окно
root = tk.Tk()
root.title("Rock-Paper-Scissors Game")

# Загрузка изображений
images = {
    "R": ImageTk.PhotoImage(Image.open(os.path.join(image_path, "rock.png")).resize((150, 150))),
    "P": ImageTk.PhotoImage(Image.open(os.path.join(image_path, "paper.png")).resize((150, 150))),
    "S": ImageTk.PhotoImage(Image.open(os.path.join(image_path, "scissors.png")).resize((150, 150)))
}

# Создание интерфейса
user_label = tk.Label(root)
user_label.grid(row=0, column=0)

computer_label = tk.Label(root)
computer_label.grid(row=0, column=2)

result_label = tk.Label(root, text="")
result_label.grid(row=1, column=1)

# Кнопки для выбора пользователя
tk.Button(root, text="Rock", command=lambda: on_user_choice("R")).grid(row=2, column=0)
tk.Button(root, text="Paper", command=lambda: on_user_choice("P")).grid(row=2, column=1)
tk.Button(root, text="Scissors", command=lambda: on_user_choice("S")).grid(row=2, column=2)

# Ползунок для настройки скорости карусели
tk.Label(root, text="Carousel speed (seconds):").grid(row=3, column=0)
speed_slider = tk.Scale(root, from_=0.1, to=2.0, orient=tk.HORIZONTAL, resolution=0.1, command=set_carousel_speed)
speed_slider.set(1.0)
speed_slider.grid(row=3, column=1)

# Переменные
user_choice = None
computer_choice = None
running = False
carousel_speed = 1.0
carousel_id = None

# Запуск приложения
root.mainloop()
