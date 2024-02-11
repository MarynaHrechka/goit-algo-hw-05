import sys


store = {}


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Error: no such name. Enter exist user name"
        except IndexError:
            return "Enter user name"

    return inner


def parse_input():
    data = input()
    cmd, *args = data.split()
    cmd = cmd.strip().lower()
    return cmd, args


def handle_command(parsed_message: list):
    match(parsed_message[0]):
        case "hello":
            print("How can I help you?")
        case "add":
            print(add_contact(parsed_message[1]))
        case "change":
            print(change_contact(parsed_message[1]))
        case "phone":
            print(show_phone(parsed_message[1][0]))
        case "all":
            print(show_all())
        case "exit":
            print("Good bye!")
            exit()
        case "close":
            print("Good bye!")
            exit()
        case _ :
            print("unknown command")


@input_error
def add_contact(data: list):
    name, phone = data
    store[name] = phone
    return "Contact added."


@input_error
def change_contact(data: list):
    name, phone = data
    store[name] = phone
    return "Contact updated."


@input_error
def show_phone(name):
    return store[name]


@input_error
def show_all():
    res = ""
    for name, phone in store.items():
        res += f"{name}: {phone}\n"
    return res


def exit():
    sys.exit(0)


def main():
    print("Welcome to the assistant bot!")
    while True:
        cmd = parse_input()
        handle_command(cmd)


main()
