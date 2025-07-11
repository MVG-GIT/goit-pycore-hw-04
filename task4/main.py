def parse_input(user_input):
    parts = user_input.strip().split()
    # Порожній ввід — повертаємо порожні значення
    if not parts:
        return "", []
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    # Недостатньо аргументів
    if len(args) < 2:
        return "Error: please provide both name and phone."
    name, phone = args[0], args[1]
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    # Недостатньо аргументів
    if len(args) < 2:
        return "Error: please provide both name and new phone."
    name, phone = args[0], args[1]
    # Номер відсутній
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."

def show_phone(args, contacts):
    # Недостатньо аргументів
    if len(args) < 1:
        return "Error: please provide a name."
    name = args[0]
    # Номер відсутній
    if name not in contacts:
        return f"Error: contact '{name}' not found."
    return contacts[name]

def show_all(contacts):
    # Номери відсутні  
    if not contacts:
        return "No contacts saved."
    # Формуємо список рядків
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    # Повертаємо рядки через переноси
    return "\n".join(lines)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
