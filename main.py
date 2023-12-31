from addr_book import *
import inspect


contacts = AddressBook()

def input_error(func):
    def handler(*args):
        argnames = func.__code__.co_varnames[:func.__code__.co_argcount]
        try:
            return func(*args)
        except KeyError:
            return "Error: key doesn't exist."
        except ValueError:
            return "Error: phone can only contain digits."
        except IndexError:
            return "Error: provide both name and phone number."
        except TypeError:
            return f"Error: provide all required parameters: {', '.join(argnames)}"
    return handler


@input_error
def hello(*args):
    return "Hi! How can I help you today?"


@input_error
def showall():
    return contacts.data


@input_error
def add(name:str, phone:str) -> None:
    if name not in contacts.data:
        name = Name(name)
        phone = Phone(phone)
        rec = Record(name, phone)
        contacts.add_record(rec)
        return f"Success! {name} has been added to your contacts list."
    else:
        contacts[name].add_phone(Phone(phone))
        return f"{phone} has been added to {name}"


@input_error
def change(name: str, old_phone: str, new_phone: str):
    if name in contacts.data:
        if contacts[name].edit_phone(old_phone, new_phone):
            return f"Phone {old_phone} for {name} has been successfully changed to {new_phone}."
        else:
            return f"Phone {old_phone} was not found."
    return f"Name was not found."


@input_error
def phone(name):
    return contacts.get_record(name)


@input_error
def delete(name, phone):
    if name not in contacts.data:
        return f"Name was not found."
    if contacts[name].del_phone(phone):
        return f"Success! {phone} has been deleted."
    else:
        return f"Phone was not found"

def main():

    func_maps = {
        "hello" : hello,
        "add" : add,
        "change" : change,
        "delete" : delete,
        "phone" : phone,
        "showall" : showall
    }

    print("Enter the first command:")
    
    while True:

        user_input = input(">>> ").lower()
        if not user_input:
            print("Error: provide a command.")
            continue

        if user_input in ["good bye", "exit", "close"]:
            print("Good bye!")
            break

        input_parts = user_input.split()
        command = input_parts[0]
        args = input_parts[1:]

        if command in func_maps:
            print(func_maps[command](*args))
        else:
            print("Command is not supported. Please choose between: hello, add, change, delete, phone or showall.")

if __name__ == "__main__":
    main()