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
def showall():
    return contacts.data


# @input_error
def add(name:str, phone:str=None, email:str=None) -> None:
    name = Name(name)
    if name.value not in contacts.data:
        phone = Phone(phone)
        email = Email(email)
        rec = Record(name, phone, email)
        contacts.add_record(rec)
        return f"Success! {name.value} has been added to your contacts list."
    return f"{name.value} already exists"


@input_error
def change(name: str, old_phone: str, new_phone: str):
    if name in contacts.data:
        result = contacts.data[name].edit_phone
        if result(old_phone,new_phone) == True:
            return f"Phone {old_phone} for {name} has been successfully changed to {new_phone}."
        else:
            return f"Phone {old_phone} was not found."
    return f"Name was not found."


@input_error
def phone(name):
    return contacts.get_record(name)


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