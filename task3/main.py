import sys
from pathlib import Path
from colorama import init, Fore, Style

def print_directory_structure(path: Path, indent: int = 0):
    prefix = '\t' * indent

    if path.is_dir():
        # Виводимо директорію синім кольором, додаючи "/" в кінці
        print(f"{prefix}{Fore.BLUE}{path.name}/" + Style.RESET_ALL)

        # Отримуємо відсортований список вмісту директорії
        try:
            for child in sorted(path.iterdir(), key=lambda p: (p.is_file(), p.name.lower())):
                print_directory_structure(child, indent + 1)
        except Exception as e:
            print(f"Сталася помилка при обробці директорії: {e}")            

    elif path.is_file():
        # Виводимо файли зеленим кольором
        print(f"{prefix}{Fore.GREEN}{path.name}{Style.RESET_ALL}")

def main():
    init(autoreset=True)  # Ініціалізація colorama з автоматичним скиданням кольорів

    if len(sys.argv) != 2:
        print(f"Очікуванний ввід: python {sys.argv[0]} /шлях/до/директорії")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"Помилка: шлях '{dir_path}' не існує.")
        sys.exit(1)

    if not dir_path.is_dir():
        print(f"Помилка: '{dir_path}' не є директорією.")
        sys.exit(1)

    print_directory_structure(dir_path)

if __name__ == "__main__":
    main()