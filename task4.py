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
    return contacts

# Головна функція
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    print("Доступні команди - add(додати контак), change(змінити існуючий контак)\n phone(Вивести телефон контакту), all (список всіх існуючих контактів)")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            result = add_contact(args, contacts)
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print(result)
        elif command == "all":
            result = show_all(contacts)
            print(result)
        else:
            print("Invalid command.")

# Запускаємо головну функцію, якщо сценарій виконується
if __name__ == "__main__":
    main()