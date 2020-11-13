import json


class ListOfContacts:
    """ List which contains objects of Contacts """
    def __init__(self):
        self.contact_list = []
        self.name_list = []
        self.lastname_list = []
        self.phone_list = []
        self.email_list = []

    def add_contact(self, *args):
        """ adds contact to list of contacts """
        if len(args) == 0:
            name = input("New Contact's name: ").capitalize()
            lastname = input("New Contact's last name: ").capitalize()
            phone = input("New Contact's phone number: ")
        else:
            name, lastname, phone = args[0], args[1], args[2]

        self.contact_list.append(Contact(name, lastname, phone))
        self.name_list.append(name)
        self.lastname_list.append(lastname)
        self.phone_list.append(phone)
        self.email_list.append(f'{name.lower()}.{lastname.lower()}@email.com')

    def search(self):
        """ compare user input with whole contact book (not sure if works) """
        search = input('Search contact book for: ').lower()

        while True:
            for i in range(len(self.name_list)):
                # print(search, self.name_list[i].lower())
                if search == self.name_list[i].lower():
                    print(self.name_list[i], self.lastname_list[i], self.phone_list[i], self.email_list[i])
                else:
                    print("didn't find any entry")
                return False
        # for info in self.name_list, self.lastname_list, self.email_list, self.phone_list:
        #     print(info)
        # if search in self.name_list, self.lastname_list, self.email_list, self.phone_list:

    def delete_contact(self):
        """ Should delete whole contact entry"""
        pass

    def print_list(self):
        # for n in [self.name_list, self.lastname_list, self.phone_list, self.email_list]:
        #     print(n)
        for entry in range(len(self.contact_list)):
            print(f"{self.name_list[entry]} {self.lastname_list[entry]}. {self.phone_list[entry]} {self.email_list[entry]}")


class Contact:
    """ contact which has name, last name, phone, email (for now) """

    def __init__(self, name, lastname, phone):
        self.name = name.capitalize()
        self.lastname = lastname.capitalize()
        self.phone = '+' + phone
        self.email = f'{self.name.lower()}.{self.lastname.lower()}@email.com'

    def return_info(self):
        return self.name, self.lastname, self.phone


class General:
    """ Main process of contact book """
    def __init__(self):
        # global contact_list
        self.list_of_contacts = ListOfContacts()

        first = Contact('Rub', 'Zur', '1671671716')
        second = Contact('Mda', 'Uj', '73676116612')
        self.list_of_contacts.add_contact(*first.return_info())
        self.list_of_contacts.add_contact(*second.return_info())

        self.app_is_running = True
        self.main_loop()

    def main_menu(self):
        print('\nWhat do you want to do?\n')
        print('1) View whole list')
        print('2) Add contact')
        print('3) Delete Contact')
        print('4) Search for specific contact\n')

    def user_input(self):
        user_inpt = input('Type one of the numbers: ')
        if user_inpt not in ['1', '2', '3', '4']:  # Поинтересоваться нумерацией функцией чтоб не надо было хардкодить
            print('Wrong input')
            return
        if user_inpt == "1":
            self.list_of_contacts.print_list()
            input()
        elif user_inpt == "2":
            self.list_of_contacts.add_contact()
            print('Successfully added new contact')


    def main_loop(self):
        while self.app_is_running:
            self.main_menu()
            self.user_input()

if __name__ == '__main__':
    letsgo = General()

    # contact_list.add_contact()
    # contact_list.print_list()
