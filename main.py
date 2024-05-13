from pathlib import Path

def parse_input(user_input):
    tokens = user_input.split()
    command = tokens[0].lower()  # перший елемент - команда
    args = tokens[1:]  # решта елементів - аргументи
    return command, args

contacts = {}

def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (KeyError, ValueError, IndexError) as e:
            print(f"Input error: {e}")
    return wrapper

@input_error
def add_contact(name, phone_number):
    contacts[name] = phone_number
    print("Contact added.")

@input_error
def change_contact(name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

@input_error
def show_phone(name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

@input_error
def show_all():
    for name, phone_number in contacts.items():
        print(f"{name}: {phone_number}")

def main():
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command == "add":
            add_contact(*args)
        elif command == "change":
            change_contact(*args)
        elif command == "phone":
            show_phone(*args)
        elif command == "all":
            show_all()
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу
		pass

class Phone(Field):
    # реалізація класу
		pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        super().__init__(value)

class Phone(Field):
    def __init__(self, value):
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Phone number must be 10 digits")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def delete_phone(self, phone):
        self.phones = [p for p in self.phones if p.value != phone]

    def edit_phone(self, old_phone, new_phone):
        self.delete_phone(old_phone)
        self.add_phone(new_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {', '.join(str(p) for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def search_by_name(self, name):
        return self.data.get(name)

    def delete_record(self, name):
        del self.data[name]

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())


address_book = AddressBook()
record1 = Record("John")
record1.add_phone("1234567890")
record2 = Record("Jane")
record2.add_phone("9876543210")
address_book.add_record(record1)
address_book.add_record(record2)
print(address_book)
