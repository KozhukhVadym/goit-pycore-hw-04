import os
import sys
from colorama import init, Fore, Style

# Ініціалізуємо colorama
init(autoreset=True)

def visualize_directory_structure(directory_path, indent=0):
    # Виводимо ім'я поточної директорії
    print(Fore.BLUE + Style.BRIGHT + ' ' * indent + os.path.basename(directory_path) + '/')

    # Ітеруємо по всім об'єктам у директорії
    for item in os.listdir(directory_path):
        item_path = os.path.join(directory_path, item)
        # Якщо це директорія, виводимо її ім'я
        if os.path.isdir(item_path):
            print(Fore.GREEN + ' ' * (indent + 4) + item + '/')
            # Рекурсивно викликаємо функцію для цієї директорії
            visualize_directory_structure(item_path, indent + 4)
        # Якщо це файл, виводимо його ім'я
        elif os.path.isfile(item_path):
            print(Fore.WHITE + ' ' * (indent + 4) + item)
        # Якщо це символічне посилання, виводимо його ім'я
        elif os.path.islink(item_path):
            print(Fore.CYAN + ' ' * (indent + 4) + item + ' (symlink)')

# Функція для перевірки та відображення структури директорії
def main():
    # Перевірка наявності аргумента командного рядка
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory_path>")
        return

    directory_path = sys.argv[1]

    # Перевірка наявності директорії за вказаним шляхом 
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print("Directory does not exist.")
        return

    visualize_directory_structure(directory_path)

if __name__ == "__main__":
    main()
