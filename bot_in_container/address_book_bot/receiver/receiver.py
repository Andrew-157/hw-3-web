from address_book_bot.decorator.inp_err_dec import input_error
from address_book_bot.classes.classes import *
from datetime import datetime


class Receiver:
    @input_error
    def add_contact(self, data, address_book: AddressBook):
        name = data.split(" ")[1]
        if name not in address_book:
            if len(data.split(" ")) == 4:
                phone = data.split(" ")[2]
                birthday = data.split(" ")[3]
                if not Phone(phone).value and not Birthday(birthday).value:
                    record = Record(name)
                    address_book[record.name.value] = record
                    return f"{name} added to the Address Book, but phone and birthday are of the wrong format.\nCall 'show_formats' command to see right formats."
                elif not Birthday(birthday).value and Phone(phone).value:
                    record = Record(name, phone)
                    address_book[record.name.value] = record
                    return f"{name} and {phone} were added to the Address Book but birthday is of the wrong format.\nCall 'show_formats' command to see right formats."
                elif Birthday(birthday).value and not Phone(phone).value:
                    record = Record(name, phone=None, birth_day=birthday)
                    address_book[record.name.value] = record
                    return f"{name} and {birthday} were added to the Address Book, but {phone} is of the wrong format.\nCall 'show_formats' command to see right formats."
                else:
                    record = Record(name, phone, birthday)
                    address_book[record.name.value] = record
                    return f"{name} with {phone} and {birthday} was added to the Address Book."
            elif len(data.split(" ")) == 3:
                phone = data.split(" ")[2]
                if Phone(phone).value:
                    record = Record(name, phone)
                    address_book[record.name.value] = record
                    return f"{name} and {phone} were added to the Address Book."
                elif not Phone(phone).value and Birthday(phone).value:
                    record = Record(name, phone=None, birth_day=phone)
                    address_book[record.name.value] = record
                    return f"{name} and {phone} birthday date were added to the Address Book."
                elif not Phone(phone).value and not Birthday(phone).value:
                    record = Record(name)
                    address_book[record.name.value] = record
                    return f"{name} was added to the Address Book, but {phone} is of the wrong format.\nCall 'show_formats' command to see right formats."
            elif len(data.split(" ")) == 2:
                record = Record(name)
                address_book[record.name.value] = record
                return f"{name} was added to the Address Book."

        else:
            return f"{name} is already in the Address Book."

    @input_error
    def add_phone(self, data, address_book: AddressBook):
        name = data.split(" ")[1]
        if name not in address_book:
            return f"{name} is not in the Address Book"
        else:
            if len(data.split(" ")) < 3 or len(data.split(" ")) > 3:
                return f"Enter {name} contact with the phone number to add."
            else:
                phone = data.split(" ")[2]
                if Phone(phone).value:
                    address_book[name].phones.append(Phone(phone))
                    return f"{phone} number was added to {name} contact."
                else:
                    return f"{phone} is of the wrong format.\nCall 'show_formats' command to see right formats."

    @input_error
    def change_phone(self, data, address_book: AddressBook):
        name = data.split(" ")[1]
        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            if len(data.split(" ")) != 4:
                return "Enter name, phone it has and new value for this phone."
            else:
                phone_to_change = data.split(" ")[2]
                new_phone = data.split(" ")[3]
                phones = [phone.value for phone in address_book[name].phones]
                if phone_to_change not in phones:
                    return f"{name} doesn't have this phone number: {phone_to_change}"
                else:
                    if not Phone(new_phone).value:
                        return f"{new_phone} is of the wrong format.\nCall 'show_formats' command to see right formats."
                    else:
                        index = phones.index(phone_to_change)
                        phones.insert(index, new_phone)
                        phones.remove(phone_to_change)
                        address_book[name].phones = []
                        for phone in phones:
                            address_book[name].phones.append(Phone(phone))
                        return f"{phone_to_change} was changed to {new_phone} for {name} contact."

    @input_error
    def delete_phones(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book"
        else:
            phones = [phone.value for phone in address_book[name].phones]
            address_book[name].phones.clear()
            return f"{phones} list for {name} contact was deleted from the Address Book."

    @input_error
    def show_all(self, data, address_book: AddressBook):
        number = data.split(" ")[1]
        info_dict = {}
        if int(number) > len(address_book):
            generator = address_book.iterator(start=0, N=len(address_book))
            for info in generator:
                try:
                    info_dict[info.name.value] = f"{[phone.value for phone in info.phones]}--{info.birth_day.value}"
                except AttributeError:
                    info_dict[info.name.value] = f"{[phone.value for phone in info.phones]}"

        else:
            generator = address_book.iterator(start=0, N=number)
            for info in generator:
                try:
                    info_dict[info.name.value] = f"{[phone.value for phone in info.phones]}--{info.birth_day.value}"
                except AttributeError:
                    info_dict[info.name.value] = f"{[phone.value for phone in info.phones]}"

        return info_dict

    @input_error
    def days_to_birthday(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            if not address_book[name].birth_day.value:
                return f"Birthday for {name} was not defined."
            else:
                date = address_book[name].birth_day.value
                date_list = date.split("-")
                reference_date = datetime(year=int(date_list[0]), month=int(
                    date_list[1]), day=int(date_list[2]))
                days_to_birthday = reference_date - datetime.now()
                return f"{days_to_birthday.days} days left to {name}'s Birthday."

    @input_error
    def change_birthday(self, data, address_book: AddressBook):
        name = data.split(" ")[1]
        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            if len(data.split(" ")) != 3:
                return f"Enter {name} and new value for its birthday date."
            else:
                birthday = data.split(" ")[2]
                if not Birthday(birthday).value:
                    return f"{birthday} is of the wrong format."
                else:
                    address_book[name].birth_day = Birthday(birthday)
                    return f"{name} contact's birthday was changed to {birthday}."

    @input_error
    def phones(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            phones = [phone.value for phone in address_book[name].phones]
            return f"{name} contact's phone list: {phones}."

    @input_error
    def birthday(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            if not address_book[name].birth_day.value:
                return f"Birthday is not defined for {name} contact."
            else:
                birthday = address_book[name].birth_day.value
                return f"{name} contact's birthday: {birthday}."

    @input_error
    def find(self, data, address_book: AddressBook):
        hint = data.split(" ")[1]
        list_to_user = []

        for name in address_book.keys():
            if hint.lower() in name.lower():
                list_to_user.append(name)
            else:
                continue

        for name, value in address_book.items():
            if name in list_to_user:
                continue
            else:
                for phone in [phone.value for phone in value.phones]:
                    if hint in phone:
                        list_to_user.append(name)

        if not list_to_user:
            return "No matches were found"
        else:
            return list_to_user

    @input_error
    def add_birthday(self, data, address_book: AddressBook):
        name = data.split(" ")[1]
        if name not in address_book:
            return f"{name} is not in the AddressBook."
        else:
            if not address_book[name].birth_day.value:
                if len(data.split(" ")) != 3:
                    return f"Enter {name} with value for birthday."
                else:
                    birthday = data.split(" ")[2]
                    if not Birthday(birthday):
                        return f"{birthday} is of the wrong format."
                    else:
                        address_book[name].birth_day = Birthday(birthday)
                        return f"{birthday} was added to {name} contact."
            else:
                return f"{name} contact already has birthday value, call 'change_birthday' command."

    @input_error
    def delete_birthday(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            if not address_book[name].birth_day.value:
                return f"{name} contact doesn't have birthday value."
            else:
                birthday = address_book[name].birth_day.value
                address_book[name].birth_day.value = None
                return f"{birthday} value was deleted for {name} contact."

    @input_error
    def delete_contact(self, data, address_book: AddressBook):
        name = data.split(" ")[1]

        if name not in address_book:
            return f"{name} is not in the Address Book."
        else:
            address_book.pop(name)
            return f"{name} contact and its information were deleted from the Address Book."

    @input_error
    def delete_all(self, data, address_book: AddressBook):
        address_book.clear()
        return f"All data from the Address Book was deleted."
