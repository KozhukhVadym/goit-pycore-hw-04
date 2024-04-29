# v_0.1
# Програма відповідає більшості вимог та поводить себе, як очікується

def add_contact(contacts, name, phone):
    contacts[name] = phone
    print("Contact added.")

def change_contact(contacts, name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def parse_input(command):
    parts = command.split()
    if len(parts) == 0:
        return None, None, None
    elif len(parts) == 1:
        return parts[0], None, None
    elif len(parts) == 2:
        return parts[0], parts[1], None
    else:
        return parts[0], parts[1], ' '.join(parts[2:])



def main():
    print("Welcome to the assistant bot!")
    contacts = {}
    
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        else:
            action, arg1, arg2 = parse_input(command)

            if action == "add":
                add_contact(contacts, arg1, arg2)
            elif action == "change":
                change_contact(contacts, arg1, arg2)
            elif action == "phone":
                show_phone(contacts, arg1)
            elif action == "all":
                show_all(contacts)
            else:
                print("Invalid command.")

if __name__ == "__main__":
    main()
