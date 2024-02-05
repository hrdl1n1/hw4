import sys
from pathlib import Path
from colorama import init, Fore

def display_directory_structure(directory_path, indent=0):
    try:
        # Отримуємо шлях до директорії:
        path = Path(directory_path)

        # Перевіряємо, чи існує директорія
        if not path.is_dir():
            print(f"{Fore.RED}Вказаний шлях не існує або не є директорією.")
            return

        # Отримуємо список об'єктів в директорії
        contents = sorted(path.iterdir())

        for item in contents:
            # Визначаємо колір для кожного об'єкта
            color = Fore.BLUE if item.is_dir() else Fore.GREEN

            # Виводимо ім'я об'єкта з кольором
            print(f"{' ' * indent}{color}{item.name}")

            # Рекурсивно викликаємо функцію
            if item.is_dir():
                display_directory_structure(item, indent + 2)

    except Exception as e:
        print(f"{Fore.RED}Помилка: {e}")

if __name__ == "__main__":
    # Ініціалізуємо colorama
    init()

    # Перевіряємо, чи передано аргумент командного рядка
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Потрібно вказати шлях до директорії.")
    else:
        # Викликаємо функцію для відображення структури директорії
        display_directory_structure(sys.argv[1])