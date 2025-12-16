# Импорты
import os
import sys

# Переменные
choice_yes = ["y","yes","да"]
choice_no = ["n","no","нет"]
choice_quit = ["q","quit","exit","выйти"]

# def quit():
#     while True:
#         if choice in choice_quit:
#             return sys.exit()

# Персонаж
class player():
    hp = 0
    mp = 0
    gold_amount = 100

    def __init__(self):
        self.name = ""
        self.prof = ""
        self.inventory = [f"{gold_amount} gold"]

# Очистка терминала
def clear():
    os.system("clear")

# Лого
def logo():
    print("============")
    print("===CANCER===")
    print("===FUCKED===")
    print("====GAME====")
    print("===FOREAL===")
    print("============\n")

# Главное меню
def main():
    clear()
    logo()
    print("1. Новая игра")
    print("2. Загрузить игру")
    print("3. Выйти из игры\n")

    choice = input("> ")
    if choice == "1":
        return new_game()
    elif choice == "2":
        # return load_game()
        input("Временно недоступно")
        return main()
    elif choice == "3":
        clear()
        return sys.exit()
    else:
        return main()

# Выбор имени
# def name_selection(target):
#     print("Введите желаемое имя")
#     target.name = input("> ")
#     print(f"Вы выбрали имя - {target.name}. Вы уверены?")
#     return somewhere

# Выбор имени новая игра
def name_selection_new_game():
    clear()
    logo()
    print("Введите желаемое имя персонажа")
    player.name = input("> ")
    print(f"Ваше имя - {player.name}. Вы уверены?")
    choice = input("> ").lower()
    if choice in choice_yes:
        return prof_selection()
    else:
        return name_selection_new_game()

# Выбор класса():
def prof_selection():
    clear()
    logo()
    print("Выберите класс персонажа:")
    print("1. Воин - Много хп, но мало мп")
    print("2. Маг - Больше мп, но меньше хп")
    choice = input("> ")
    if choice == "1":
        print("Ваш класс - Воин. Вы уверены?")
        choice = input("> ").lower()
        if choice in choice_yes:
            player.prof = "Воин"
            player.hp = 120
            player.mp = 80
            return new_game_confirm()
        else:
            return prof_selection()
    elif choice == "2":
        print("Ваш класс - Маг. Вы уверены?")
        choice = input("> ").lower()
        if choice in choice_yes:
            player.prof = "Маг"
            player.hp = 80
            player.mp = 120
            return new_game_confirm()
        else:
            return prof_selection()
    else:
        input("Попробуйте снова")
        return prof_selection()

# Подтверждение
def new_game_confirm():
    clear()
    logo()
    print(f"Ваше имя - {player.name}. Ваш класс - {player.prof}. Вы уверены?")
    choice = input("> ").lower()
    if choice in choice_yes:
        # new_game_start()
        input("WIP")
        return main()
    elif choice in choice_no:
        return name_selection_new_game()
    else:
        return new_game_confirm()

# Новая игра
def new_game():
    print("Ваши данные будут удалены. Вы уверены?")
    choice = input("> ").lower()
    if choice in choice_yes:
        return name_selection_new_game()
    else:
        return main()

if __name__ == "__main__":
    main()

