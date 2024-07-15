"""
Бот повинен перебувати в нескінченному циклі, чекаючи команди користувача.
Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", та відповідає у консоль повідомленням "How can I help you?"
"add username phone". За цією командою бот зберігає у пам'яті, наприклад у словнику, новий контакт. Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.
"change username phone". За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username, що вже існує в записнику.
"phone username" За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
"all". За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
"close", "exit" за будь-якою з цих команд бот завершує свою роботу після того, як виведе у консоль повідомлення "Good bye!" та завершить своє виконання.
Логіка команд реалізована в окремих функціях і ці функції приймають на вхід один або декілька рядків та повертають рядок.
Вся логіка взаємодії з користувачем реалізована у функції main, всі print та input відбуваються тільки там.
"""
from typing import Dict
from io import StringIO 
from unittest.mock import patch

def parse_input(user_input: str) -> tuple:
    """
    Parses the user input into a command and its arguments.
    
    Parameters:
    - user_input (str): The raw input string from the user.
    
    Returns:
    - tuple: A tuple where the first element is the command (str) and the rest are arguments (list of str).
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Adds a new contact to the contacts dictionary.
    
    Parameters:
    - args (tuple): A tuple containing the name and phone number of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A message indicating the contact was added.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Changes the phone number of an existing contact.
    
    Parameters:
    - args (tuple): A tuple containing the name and new phone number of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A message indicating the contact was updated or not found.
    """
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."

def show_phone(args: tuple, contacts: Dict[str, str]) -> str:
    """
    Retrieves the phone number of a specified contact.
    
    Parameters:
    - args (tuple): A tuple containing the name of the contact.
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: The phone number of the contact or a message indicating the contact was not found.
    """
    name, *_ = args
    if name in contacts:
        return contacts[name]
    return "Contact not found."

def show_all(contacts: Dict[str, str]) -> str:
    """
    Returns a string representation of all contacts.
    
    Parameters:
    - contacts (Dict[str, str]): The dictionary of contacts.
    
    Returns:
    - str: A string representation of the contacts dictionary.
    """
    return str(contacts)

def main():
    """
    The main function of the assistant bot. It initializes the contacts dictionary and processes user commands.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command.lower() in ["close", "exit", "quit", "q"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
            
# add block with tests for the functions
def test_functions():
    contacts = {}
    assert add_contact(("John", "123456"), contacts) == "Contact added."
    assert add_contact(("Alice", "987654"), contacts) == "Contact added."
    assert add_contact(("John", "098765"), contacts) == "Contact added."
    assert change_contact(("John", "098765"), contacts) == "Contact updated."
    assert change_contact(("Bob", "123456"), contacts) == "Contact not found."
    assert show_phone(("John",), contacts) == "098765"
    assert show_phone(("Alice",), contacts) == "987654"
    assert show_phone(("Bob",), contacts) == "Contact not found."
    assert show_all(contacts) == "{'John': '098765', 'Alice': '987654'}"
    print("All function tests passed.")
    
def test_main():
    # Define test data as a list of tuples, where each tuple contains a user input and the expected output.
    test_data = [
        ("hello", "How can I help you?"),  # Test greeting
        ("add John 123456", "Contact added."),  # Test adding a new contact
        ("phone John", "123456"),  # Test retrieving a contact's phone number
        ("change John 098765", "Contact updated."),  # Test changing a contact's phone number
        ("phone John", "098765"),  # Test retrieving the updated phone number
        ("all", "{'John': '098765'}"),  # Test displaying all contacts
        ("wrong_command", "Invalid command."),  # Wrong command
        ("close", "Good bye!")  # Test closing the application
    ]
    # Patch the input function to simulate user input based on the test data.
    with patch("builtins.input", side_effect=[i[0] for i in test_data]):
        # Patch sys.stdout to capture the output of the main function.
        with patch("sys.stdout", new_callable=StringIO) as fake_out:
            main()  # Call the main function to process the simulated user input.
            # Assert that the captured output matches the expected output defined in the test data.
            expected_output = f"Welcome to the assistant bot!\n{'\n'.join([i[1] for i in test_data])}".strip().split('\n')
            actual_output = fake_out.getvalue().strip().split('\n')
            assert actual_output == expected_output, \
                "Test main function is failed output is not equal to expected"
    print("The main function tests passed.")
            
# Uncomment the line below to run the tests
# test_functions()
# test_main()
            
if __name__ == "__main__":
    main()
    
# Usage example:

# Welcome to the assistant bot!
# Enter a command: hello
# bot answer: How can I help you?
# Enter a command: add John 123456
# bot answer: Contact added.
# Enter a command: phone John
# bot answer: 123456
# Enter a command: change John 098765
# bot answer: Contact updated.
# Enter a command: phone John
# bot answer: 098765
# Enter a command: all
# bot answer: {'John': '098765'}
# Enter a command: close, exit, quit, q
# bot answer:  Good bye!