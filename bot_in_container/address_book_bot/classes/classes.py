import re
from collections import UserDict
import pickle


class Birthday:
    def __init__(self, birth_day):
        self.__value = None
        self.value = birth_day

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, birth_day):
        check_match = re.search(r"[0-9]{4}\-[0-9]{2}\-[0-9]{2}", birth_day)
        if check_match:
            self.__value = birth_day
        else:
            self.__value = None


class Phone:
    def __init__(self, phone):
        self.__value = None
        self.value = phone

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, phone):
        check_match = re.search(
            r"\([0-9]{2}\)\-[0-9]{3}\-[0-9]{1}\-[0-9]{3}|\([0-9]{2}\)\-[0-9]{3}\-[0-9]{2}\-[0-9]{2}", phone)
        if check_match:
            self.__value = phone
        else:
            self.__value = None


class Name:
    def __init__(self, name):
        self.value = name


class Record:
    def __init__(self, name, phone=None, birth_day=None):
        self.name = Name(name)

        if phone and birth_day:

            self.phones = [Phone(phone)]
            self.birth_day = Birthday(birth_day)

        elif not phone and not birth_day:

            self.phones = []
            self.birth_day = None

        elif not phone and birth_day:

            self.phones = []
            self.birth_day = Birthday(birth_day)

        elif phone and not birth_day:

            self.phones = [Phone(phone)]
            self.birth_day = None


class AddressBook(UserDict):
    def iterator(self, start, N):
        keys = list(self.data.keys())
        while int(start) < int(N):
            yield self.data[keys[start]]
            start += 1

    def load_address_book(self):
        try:
            object = self
            with open("address_book.txt", "rb") as file:
                object = pickle.load(file)
            return object
        except FileNotFoundError:
            object = self
            return object

    def dump_address_book(self, address_book):
        with open("address_book.txt", "wb") as file:
            pickle.dump(address_book, file)
