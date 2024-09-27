import tkinter
import PIL
import random

def play_rps():
    # Возможные варианты выбора
    choices = ["R", "P", "S"]
    
    while True:
        # Пользователь делает выбор
        user_choice = input("Choose: R (Rock), P (Paper), S (Scissors): ").upper()
        
        # Проверяем, ввёл ли пользователь правильное значение
        if user_choice not in choices:
            print("The choice is wrong! Please try again")
            continue  # Возвращаемся к началу цикла, чтобы запросить новый ввод
        
        # Компьютер делает случайный выбор
        computer_choice = random.choice(choices)
        
        # Выводим выбор компьютера
        print(f"Computer choice: {computer_choice}")
        
        # Определяем результат игры
        if user_choice == computer_choice:
            print("Tie!")
        elif (user_choice == "R" and computer_choice == "S") or \
             (user_choice == "S" and computer_choice == "P") or \
             (user_choice == "P" and computer_choice == "R"):
            print("Amazing! You are win!")
        else:
            print("Oh! Computer is win!")
        
        # Спрашиваем пользователя, хочет ли он продолжить игру
        play_again = input("Do you want play again? (yes/no):").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break  # Выходим из цикла и завершаем игру

# Запуск игры
play_rps()