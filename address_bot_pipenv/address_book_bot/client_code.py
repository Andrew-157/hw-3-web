from address_book_bot.classes.classes import *
from address_book_bot.commands.commands import *
from address_book_bot.interface.interface import *


class Invoker:

    def execute_command(self, command: ICommand):
        return command.execute()


def client_code():
    address_book = AddressBook().load_address_book()
    user = Invoker()
    while True:
        user_input = input("Enter a command: ")
        if user_input.split(" ")[0].lower() in COMMANDS_1:
            command = user_input.split(" ")[0]
            print(user.execute_command(COMMANDS_1[command.lower()]()))

        elif user_input.split(" ")[0].lower() in ["delete_all", "delete_phones", "delete_contact", "delete_birthday"]:
            user_choice = input(
                "Are you sure you want this command to be executed?(Y/n): ")
            if user_choice.lower() in ["yes", "y"]:
                command = user_input.split(" ")[0]
                print(user.execute_command(COMMANDS[command.lower()](
                    user_input, Receiver(), address_book)))
            elif user_choice.lower() in ["no", "n"]:
                print("Ok")
                continue
            else:
                user_choice = input(
                    "Are you sure you want this command to be executed?(Y/n): ")
                if user_choice.lower() in ["yes", "y"]:
                    command = user_input.split(" ")[0]
                    print(user.execute_command(COMMANDS[command.lower()](
                        user_input, Receiver(), address_book)))
                elif user_choice.lower() in ["no", "n"]:
                    print("Ok")
                    continue
        elif user_input.split(" ")[0] in COMMANDS:
            command = user_input.split(" ")[0]
            print(user.execute_command(COMMANDS[command.lower()](
                user_input, Receiver(), address_book)))
        elif user_input.split(" ")[0].lower() in ["exit", "goodbye", "close"]:
            AddressBook().dump_address_book(address_book)
            print("Address Book was saved to file: 'address_book.txt'")
            print("Goodbye")
            break
        else:
            print("No such a command")
            print("Use 'commands' command to see all the commands.")


if __name__ == "__main__":
    client_code()

client_code()
