"""
Завдання 1

У вас є текстовий файл, який містить інформацію про місячні заробітні плати розробників у вашій компанії. Кожен рядок у файлі містить прізвище розробника та його заробітну плату, які розділені комою без пробілів.

Наприклад:

Alex Korp,3000
Nikita Borisenko,2000
Sitarama Raju,1000
Ваше завдання - розробити функцію total_salary(path), яка читає цей файл та повертає кортеж з двома значеннями:

"""
from typing import Tuple
import pathlib

TEST_DATA_DIR = (pathlib.Path(__file__).parent).joinpath("test_data")


def total_salary(path: str) -> Tuple[int, int]:
    """
    Calculates the total salary and the average salary from a file.
    
    The function reads a file specified by the path. Each line in the file should contain
    employee data separated by commas, where the second value is the salary (an integer).
    It calculates the total sum of all salaries and the average salary.
    If the file is empty, both values in the tuple will be 0.
    If the file does not exist or is corrupted, the function will print an error message.
    
    Parameters:
    - path (str): The path to the file containing employee data.
    
    Returns:
    - Tuple[int, int]: A tuple containing the total sum of salaries and the average salary.
    """
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                count += 1
                try:
                    total += int(line.split(',')[1])
                except IndexError:
                    print(f"File data '{line}' is corrupted")
                    total += 0
    except FileNotFoundError:
        print("File not found")
    except ValueError:
        print("File is corrupted")
    try:
        return total, total // count if count else 0
    except ZeroDivisionError:
        print("File is empty")
        return 0, 0

# Test function with test cases
def test_total_salary():
    # Test case 1: Check for correct total and average salary
    total, average = total_salary(pathlib.PurePath(TEST_DATA_DIR, "salary_file.txt"))
    assert total == 6000 and average == 2000, "Test case 1 failed"
    
    # Test case 2: Check for file not found
    total, average = total_salary(pathlib.PurePath(TEST_DATA_DIR, "salary_file1.txt"))
    assert total == 0 and average == 0, "Test case 2 failed"
    
    # Test case 3: Check for corrupted file
    total, average = total_salary(pathlib.PurePath(TEST_DATA_DIR, "salary_file_invalid.txt"))
    assert total == 6000 and average == 1500, "Test case 3 failed"
    
    # Test case 4: Check for empty file
    total, average = total_salary(pathlib.PurePath(TEST_DATA_DIR, "salary_file_empty.txt"))
    assert total == 0 and average == 0, "Test case 4 failed"
    print("All test cases passed successfully.")
    
# Uncomment the line below to run the test function
# test_total_salary()
