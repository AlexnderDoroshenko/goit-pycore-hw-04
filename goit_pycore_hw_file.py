"""
У вас є текстовий файл, який містить інформацію про котів. Кожен рядок файлу містить унікальний ідентифікатор кота, його ім'я та вік, розділені комою. Наприклад:

60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5

Ваше завдання - розробити функцію get_cats_info(path), яка читає цей файл та повертає список словників з інформацією про кожного кота.



Вимоги до завдання:

Функція get_cats_info(path) має приймати один аргумент - шлях до текстового файлу (path).
Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
Функція має повертати список словників, де кожен словник містить інформацію про одного кота.


Рекомендації для виконання:

Використовуйте with для безпечного читання файлу.
Пам'ятайте про встановлення кодування при відкриті файлів
Для кожного рядка в файлі використовуйте split(',') для отримання ідентифікатора, імені та віку кота.
Утворіть словник з ключами "id", "name", "age" для кожного кота та додайте його до списку, який буде повернуто.
Опрацьовуйте можливі винятки, пов'язані з читанням файлу.


Критерії оцінювання:

Функція має точно обробляти дані та повертати правильний список словників.
Повинна бути належна обробка винятків і помилок.
Код має бути чистим, добре структурованим і зрозумілим.


Приклад використання функції:

cats_info = get_cats_info("path/to/cats_file.txt")
print(cats_info)



Очікуваний результат:

[
    {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
    {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
    {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
    {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
    {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
]
"""
from typing import List
import pathlib

TEST_DATA_DIR = (pathlib.Path(__file__).parent).joinpath("test_data")

def get_cats_info(path: str) -> List[dict]:
    """
    Reads the file and returns a list of dictionaries with information about each cat 
    If the file is not found or corrupted, returns an empty list

    Args:
        path (str): Path to the file

    Returns:
        List[dict]: List of dictionaries with information about each cat
    """
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat = line.strip().split(',')
                if is_data_valid(cat):
                    cats_info.append({"id": cat[0], "name": cat[1], "age": cat[2]})
                else:
                    print(f"File '{path}' value '{cat}' is corrupted")
    except FileNotFoundError:
        print(f"File '{path}' not found")
    except ValueError:
        print(f"File '{path}' value is corrupted")
    return cats_info

def is_data_valid(data: list) -> bool:
    """
    Check if the data is valid

    Args:
        data (List): List of information about the cat

    Returns:
        bool: True if the data is valid, False otherwise
    """
    # three values in the list
    if not len(data) == 3:
        return False
    # check the values not empty
    if not all(data):
        return False
    # check the values are the correct type
    if not all(isinstance(value, str) for value in data):
        return False
    #check the age is a number
    if not data[2].isdigit():
        return False
    # check the age is a positive number
    if not int(data[2]) > 0:
        return False
    #   check the id is a valid id
    if not len(data[0]) == 24:
        return False
    # check the id is a valid hexadecimal number
    try:
        int(data[0], 16)
    except ValueError:
        return False
    return True

# Test function with test cases
def test_get_cats_info():
    # Test case 1: Check for correct cats info
    cats_expected_info = [
        {"id": "60b90c1c13067a15887e1ae1", "name": "Tayson", "age": "3"},
        {"id": "60b90c2413067a15887e1ae2", "name": "Vika", "age": "1"},
        {"id": "60b90c2e13067a15887e1ae3", "name": "Barsik", "age": "2"},
        {"id": "60b90c3b13067a15887e1ae4", "name": "Simon", "age": "12"},
        {"id": "60b90c4613067a15887e1ae5", "name": "Tessi", "age": "5"},
    ]
    cats_actual_info = get_cats_info(pathlib.PurePath(TEST_DATA_DIR, "cats_file.txt"))
    assert cats_actual_info == cats_expected_info, "Test correct cats info case 1 failed"
    
    # Test case 2: Check for file not found
    cats_info = get_cats_info(pathlib.PurePath(TEST_DATA_DIR, "cats_file1.txt"))
    assert cats_info == [], "Test file not found case 2 failed"
    
    # Test case 3: Check for corrupted file
    cats_info = get_cats_info(pathlib.PurePath(TEST_DATA_DIR, "cats_file2.txt"))
    cats_expected_broken_info = [
        {'id': '60b90c1c13067a15887e1ae1', 'name': 'Tayson', 'age': '3'},
        {'id': '60b90c2413067a15887e1ae2', 'name': 'Vika', 'age': '1'},
        {'id': '60b90c2e13067a15887e1ae3', 'name': 'Barsik', 'age': '2'},
        {'id': '60b90c3b13067a15887e1ae4', 'name': 'Simon', 'age': '12'}
    ]
    assert cats_info == cats_expected_broken_info, "Test corrupted file data case 3 failed"
    print("All test cases passed successfully")

# Uncomment the line below to run the test function
# test_get_cats_info()
