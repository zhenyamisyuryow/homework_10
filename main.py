from addr_book import *


contacts = AddressBook()

def input_error(func):
    def handler(*args):
        try:
            return func(*args)
        except KeyError:
            return "Error: key doesn't exist."
        except ValueError:
            return "Error: phone can only contain digits."
        except IndexError:
            return "Error: provide both name and phone number."
        except TypeError as e:
            return e
    return handler


@input_error
def hello(*args):
    return "Hi! How can I help you today?"


@input_error
def add(*args) -> None:
    name = Name(args[0])
    if name.value not in contacts.data:
        phone = Phone(args[1])
        rec = Record(name, phone)
        contacts.add_record(rec)
        return f"Success! {name.value} has been added to your contacts list."
    return f"{name.value} already exists"


@input_error
def showall():
    return contacts.data


@input_error
def change(name: str, old_phone: str, new_phone: str):
    if name in contacts.data:
        return contacts.data[name].edit_phone(old_phone, Phone(new_phone))
    return f"Name was not found"


@input_error
def phone(name):
    return contacts.data[name].phones


def main():

    func_maps = {
        "hello" : hello,
        "add" : add,
        "change" : change,
        "phone" : phone,
        "showall" : showall
    }

    print("Enter the first command:")
    
    while True:

        user_input = input(">>> ").lower()

        if user_input in ["good bye", "exit", "close"]:
            print("Good bye!")
            break

        input_parts = user_input.split()
        command = input_parts[0]
        args = input_parts[1:]

        if command in func_maps:
            print(func_maps[command](*args))
        else:
            print("Command is not supported. Please choose between: hello, add, change, phone or showall.")

if __name__ == "__main__":
    main()