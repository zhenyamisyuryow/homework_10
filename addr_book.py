from collections import UserDict

class AddressBook(UserDict):

    def add_record(self, record):
        key = record.name.value
        value = record
        self.data[key] = value
    
    def change_record(self, record):
        self.data[record.name.value] = record
    
    def get_record(self, name):
        return f"{self.data[name]}"
    


class Name:
    def __init__(self, value):
        self.value = value


class Phone:
    def __init__(self, value):
        self.value = value
    
    def __repr__(self):
        return f"{self.value}"
    

class Email:
    def __init__(self, value):
        self.value = value
        
    def __repr__(self):
        return f"{self.value}"


class Record:
    def __init__(self, name:Name, phone:Phone = None, email:Email = None):
        self.name = name
        self.phones = list()
        self.phones.append(phone)
        self.email = email
    
    def __repr__(self):
        return f"Name: {self.name.value}, Phones: {self.phones}, Email: {self.email}"
    
    def add_phone(self, new_phone):
        self.phones.append(new_phone)
    
    def del_phone(self, phone):
        self.phones.remove(phone)
    
    def edit_phone(self,old_phone, new_phone):
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone
                return True
        return False