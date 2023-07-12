from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        key = record.name.value
        value = record
        self.data[key] = value
    
    def change_record(self, record):
        self.data[record.name] = record
    
    def get_record(self, record):
        return f"{self.data[record.name]}"
    

class Name:
    def __init__(self, value):
        self.value = value


class Phone:
    def __init__(self, phone):
        self.phone = phone
    
    def __repr__(self):
        return f"{self.phone}"


class Record:
    def __init__(self, name, phone = None, email = None):
        self.name = name
        self.phones = list()
        self.phones.append(phone)
    
    def __repr__(self):
        return f"Name: {self.name.value}, Phones: {self.phones}"
    
    def add_phone(self, new_phone):
        return self.phones.append(new_phone)
    
    def del_phone(self, phone):
        return self.phones.remove(phone)
    
    def edit_phone(self,old_phone, new_phone):
        index = self.phones.index(str(old_phone))
        self.phones[index] = new_phone
        return self.phones
    