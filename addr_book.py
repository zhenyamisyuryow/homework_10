from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        key = record.name.value
        value = record
        self.data[key] = value
        
    def get_record(self, name):
        return f"{self.data[name].phones}"
    
    
class Field:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"

class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
    

class Email(Field):
    def __init__(self, value):
        super().__init__(value)


class Record:
    def __init__(self, name:Name, phone:Phone = ''):
        self.name = name
        self.phones = list()
        self.phones.append(phone)
    
    def add_phone(self, new_phone):
        self.phones.append(new_phone)
    
    def edit_phone(self, old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return True
        return False
    
    def del_phone(self, phone):
        for item in self.phones:
            if item.value == phone:
                self.phones.remove(item)
                return True
        return False
    
    def __repr__(self):
        return f"Name: {self.name.value}, Phones: {self.phones}"