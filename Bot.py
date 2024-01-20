from AddressBook import *
from abc import ABC, abstractmethod
from Note import Note


class AbstractBot(ABC):
    def __init__(self):
        self.book = AddressBook()

    @abstractmethod
    def handle(self, action):
        pass


class AddBot(AbstractBot):

    def handle(self, book):  # add book
        self.book = book
        record = self.create_record()
        return self.book.add(record)

    def create_record(self):
        name = Name(input("Name: ")).value.strip()
        phones = Phone().value
        birth = Birthday().value
        email = Email().value.strip()
        status = Status().value.strip()
        note = Note(input("Note: ")).value
        record = Record(name, phones, birth, email, status, note)
        print(self.book)
        return record


class SearchBot(AbstractBot):
    def handle(self, book):  # delete "action", add book
        self.book = book
        print("There are following categories: \nName \nPhones \nBirthday \nEmail \nStatus \nNote")
        category = input('Search category: ')
        pattern = input('Search pattern: ')
        result = self.book.search(category, pattern)
        self.display_result(result)

    def display_result(self, result):
        for account in result:
            if account['birthday']:
                birth = account['birthday'].strftime("%d/%m/%Y")
                result_str = "_" * 50 + "\n" + \
                    f"Name: {account['name']} \nPhones: {', '.join(account['phones'])} \nBirthday: {birth} \nEmail: {account['email']} \nStatus: {account['status']} \nNote: {account['note']}\n" + "_" * 50
                print(result_str)


class EditBot(AbstractBot):
    def handle(self, book):  # add book
        self.book = book
        contact_name = input('Contact name: ')
        parameter = input(
            'Which parameter to edit(name, phones, birthday, status, email, note): ').strip()
        new_value = input("New Value: ")
        result = self.book.edit(contact_name, parameter, new_value)
        return result


class RemoveBot(AbstractBot):
    def handle(self, book):  # add book
        self.book = book
        pattern = input("Remove (contact name or phone): ")
        return self.book.remove(pattern)


class SaveBot(AbstractBot):
    def handle(self, book):  # add book
        self.book = book
        file_name = input("File name: ")
        return self.book.save(file_name)


class LoadBot(AbstractBot):
    def handle(self, book):  # delete "action", add book
        self.book = book
        file_name = input("File name: ")
        return self.book.load(file_name)


class CongratulateBot(AbstractBot):
    def handle(self, book):   # add book
        self.book = book
        print(self.book.congratulate())


class ViewBot(AbstractBot):
    def handle(self, book):   # add book
        self.book = book
        print(self.book)


class ExitBot(AbstractBot):
    def handle(self, book):  # add book
        self.book = book
        print("Bye")
        exit()
