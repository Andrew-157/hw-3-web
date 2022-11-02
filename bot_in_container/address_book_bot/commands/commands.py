from address_book_bot.interface.interface import ICommand
from address_book_bot.receiver.receiver import Receiver
from address_book_bot.classes.classes import *


class SayHelloCommand(ICommand):

    def execute(self):
        return "How can I help you?"


class AddContactCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.address_book = address_book
        self.receiver = receiver

    def execute(self):
        return self.receiver.add_contact(self.data, self.address_book)


class AddPhoneCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.add_phone(self.data, self.address_book)


class ChangePhoneCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.change_phone(self.data, self.address_book)


class DeletePhonesCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.delete_phones(self.data, self.address_book)


class ShowAllCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.show_all(self.data, self.address_book)


class DaysToBirthdayCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.days_to_birthday(self.data, self.address_book)


class ChangeBirthdayCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.change_birthday(self.data, self.address_book)


class ShowPhonesCommand(ICommand):
    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.phones(self.data, self.address_book)


class ShowBirthdayCommand(ICommand):
    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.birthday(self.data, self.address_book)


class FindCommand(ICommand):
    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.find(self.data, self.address_book)


class AddBirthday(ICommand):
    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.add_birthday(self.data, self.address_book)


class DeleteBirthdayCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.delete_birthday(self.data, self.address_book)


class DeleteContactCommand(ICommand):
    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.data = data
        self.receiver = receiver
        self.address_book = address_book

    def execute(self):
        return self.receiver.delete_contact(self.data, self.address_book)


class ClearBookCommand(ICommand):

    def __init__(self, data, receiver: Receiver, address_book: AddressBook):
        self.address_book = address_book
        self.data = data
        self.receiver = receiver

    def execute(self):
        return self.receiver.delete_all(self.data, self.address_book)


class ShowCommandsCommand(ICommand):

    def execute(self):
        return list(COMMANDS.keys()) + list(COMMANDS_1.keys())


class ShowFormatsCommand(ICommand):

    def execute(self):
        return f"Birthday format is: yyyy-mm-dd,\nphone formats are: (00)-000-0-000 or (00)-000-00-00."


COMMANDS = {"add": AddContactCommand,
            "add_phone": AddPhoneCommand,
            "change_phone": ChangePhoneCommand,
            "delete_phones": DeletePhonesCommand,
            "show_all": ShowAllCommand,
            "days_to_birthday": DaysToBirthdayCommand,
            "change_birthday": ChangeBirthdayCommand,
            "phones": ShowPhonesCommand,
            "birthday": ShowBirthdayCommand,
            "find": FindCommand,
            "add_birthday": AddBirthday,
            "delete_birthday": DeleteBirthdayCommand,
            "delete_contact": DeleteContactCommand,
            "delete_all": ClearBookCommand,
            }

COMMANDS_1 = {"hello": SayHelloCommand,
              "commands": ShowCommandsCommand,
              "show_formats": ShowFormatsCommand}
