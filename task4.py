def parse_input(user_input):
    # Розбиваємо введення користувача на команду та аргументи, видаляємо початкові та кінцеві пробіли, нижній регістр 
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

# Функція для додавання контакту до словника контактів
def add_contact(args, contacts):
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid number of arguments for 'add' command."

# Функція для зміни номеру телефону існуючого контакту
def change_contact(args, contacts):
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid number of arguments for 'change' command."

# Функція для відображення номера телефону конкретного контакту
def show_phone(args, contacts):
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid number of arguments for 'phone' command."

# Функція відображає всі контакти та їх номери телефонів
def show_all(contacts):
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

# Головна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
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
            show_all(contacts)
        else:
            print("Invalid command.")

# Запускаємо головну функцію, якщо сценарій виконується
if __name__ == "__main__":
    main()