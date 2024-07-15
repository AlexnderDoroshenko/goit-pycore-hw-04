"""
Розробіть скрипт, який приймає шлях до директорії в якості аргументу командного рядка і візуалізує структуру цієї директорії, виводячи імена всіх піддиректорій та файлів. Для кращого візуального сприйняття, імена директорій та файлів мають відрізнятися за кольором.



Вимоги до завдання:

Створіть віртуальне оточення Python для ізоляції залежностей проекту.
Скрипт має отримувати шлях до директорії як аргумент при запуску. Цей шлях вказує, де знаходиться директорія, структуру якої потрібно відобразити.
Використання бібліотеки colorama для реалізації кольорового виведення.
Скрипт має коректно відображати як імена директорій, так і імена файлів, використовуючи рекурсивний спосіб обходу директорій (можна, за бажанням, використати не рекурсивний спосіб).
Повинна бути перевірка та обробка помилок, наприклад, якщо вказаний шлях не існує або він не веде до директорії.


Рекомендації для виконання:

Спочатку встановіть бібліотеку colorama. Для цього створіть та активуйте віртуальне оточення Python, а потім встановіть пакет за допомогою pip.
Використовуйте модуль sys для отримання шляху до директорії як аргументу командного рядка.
Для роботи з файловою системою використовуйте модуль pathlib.
Забезпечте належне форматування виводу, використовуючи функції colorama.


Критерії оцінювання:

Створення та використання віртуального оточення.
Правильність отримання та обробки шляху до директорії.
Точність виведення структури директорії.
Коректне застосування кольорового виведення за допомогою colorama.
Якість коду, включаючи читабельність, структурування та коментарі.


Приклад використання:

Якщо виконати скрипт та передати йому абсолютний шлях до директорії як параметр.

python hw03.py /шлях/до/вашої/директорії

Це призведе до виведення в терміналі списку всіх піддиректорій та файлів у вказаній директорії з використанням різних кольорів для піддиректорій та файлів, що полегшить візуальне сприйняття файлової структури.

Для директорії зі наступною структурою

📦picture
 ┣ 📂Logo
 ┃ ┣ 📜IBM+Logo.png
 ┃ ┣ 📜ibm.svg
 ┃ ┗ 📜logo-tm.png
 ┣ 📜bot-icon.png
 ┗ 📜mongodb.jpg

Скрипт повинен вивести схожу структуру

"""
import sys
from pathlib import Path
from colorama import Fore, Style
from io import StringIO
from pathlib import Path
import tempfile
import shutil

TEST_DATA_DIR = (Path(__file__).parent).joinpath("test_data")

def print_dir_tree(path: Path, prefix: str = ''):
    """
    Prints the directory tree starting from the given path, displaying directories first and files last,
    with branches, including the parent directory.
    
    Parameters:
    - path (Path): The root directory or file to start the tree from.
    - prefix (str): The prefix to use for indentation and branches.
    """
    # Print the parent directory
    if prefix == '':  # This ensures the parent directory is printed only once
        print(Fore.BLUE + f'📦 {path.name}' + Style.RESET_ALL)
    
    items = list(path.iterdir()) if path.is_dir() else []
    directories = [item for item in items if item.is_dir()]
    files = [item for item in items if item.is_file()]

    # Continue with the existing logic to print directories and files
    items_sorted = directories + files  # Directories first, then files

    for i, item in enumerate(items_sorted):
        is_last = i == len(items_sorted) - 1  # Check if the item is the last in the list
        connector = "└── " if is_last else "├── "
        if item.is_dir():
            # Print directory with a blue color
            print(Fore.BLUE + prefix + connector + f'📂 {item.name}' + Style.RESET_ALL)
            # Prepare new prefix for the next level, depending on whether the item is the last
            new_prefix = prefix + ("    " if is_last else "│   ")
            print_dir_tree(item, new_prefix)
        else:
            # Print file with a green color
            print(Fore.GREEN + prefix + connector + f'📜 {item.name}' + Style.RESET_ALL)
            

# Test function with test cases

def test_print_dir_tree():
    # Create a temporary directory
    temp_dir =tempfile.mkdtemp()
    # Create subdirectories and files
    (Path(temp_dir) / "dir1").mkdir()
    (Path(temp_dir) / "dir1" / "file1.txt").touch()
    (Path(temp_dir) / "file2.txt").touch()
    # Capture the original stdout
    original_stdout = sys.stdout
    sys.stdout = StringIO()
    # Run the function
    print_dir_tree(Path(temp_dir))
    # Get the captured output
    output = str(sys.stdout.getvalue()).strip()
    # Define the expected output
    expected_output = f"📦 {Path(temp_dir).name}\n    ├── 📂 dir1\n    │   └── 📜 file1.txt\n    └── 📜 file2.txt\n".strip()
    # Assert the output
    for line in expected_output:
        assert line in output, f"Expected line: \n{line} \nnot in output: \n{output}"
    # Restore the original stdout
    sys.stdout = original_stdout
    # Remove the temporary directory
    shutil.rmtree(temp_dir)
    
    print("All test cases passed successfully.")
            
def main():
    """
    Main function that processes command line arguments and starts the directory tree printing.
    """
    # Check if exactly one argument (the directory path) is provided.
    if len(sys.argv) != 2:
        print("Usage: python hw03.py <directory>")
        sys.exit(1)
    path = Path(sys.argv[1])
    # Check if the provided path exists.
    if not path.exists():
        print(f"Error: {path} does not exist.")
        sys.exit(1)
    # Start printing the directory tree from the provided path.
    print_dir_tree(path)
    
#Uncomment the following line to run the test function
# test_print_dir_tree()

if __name__ == "__main__":
    main()
