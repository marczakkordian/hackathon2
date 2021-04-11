import json

# init list and dict
contact_list = []
entry_dict = {'Olaf Skiba': 123456789}
contact_list.append(entry_dict)

# load or create json file
filename = 'numbers_book.json'
with open(filename, 'w+') as f:
    json.dump(contact_list, f, indent=100, allow_nan=False)


def save_to_file(list):
    with open(filename, 'w') as f:
        json.dump(contact_list, f)


def load_list_of_entries():
    print('---> Show all contacts  is open <----')
    try:
        with open(filename, 'r') as f:
            contact_list = json.load(f)
        counter = len(contact_list)
    except FileNotFoundError:
        contact_list = []

    if counter > 0:
        print(f'The amount of entries: {counter}')
        print(contact_list)
    else:
        print('Contact list is empty! There is nothing to show...')
    return contact_list
    print('---> Show all contacts is closed <----')


def add_contact(list):
    print('---> Add contact is open <----')
    full_name = str(input('Enter name: '))
    while True:
        try:
            phone_number = int(input('Enter phone number: '))
            add_entry = {full_name: phone_number}
            contact_list.append(add_entry)
        except ValueError as err:
            print('That was no valid number. Try again: ', err)
    print('---> Add contact is closed <----')


# main code
if __name__ == '__main__':
    contact_list = load_list_of_entries()
    while True:
        usr_answer = input('Do you want add new entry? [y/n]')
        if usr_answer == 'y':
            add_contact(contact_list)
            save_to_file(contact_list)
            load_list_of_entries()
        elif usr_answer == 'n':
            break
        else:
            add_contact(contact_list)
            save_to_file(contact_list)
            load_list_of_entries()
