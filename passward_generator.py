import string
from secrets import choice


def main(user_input):
    print('//////////////////////////////////////////////////////////////////////////////')
    print('                 Greetings! Welcome to passwords generator                     ')
    print('//////////////////////////////////////////////////////////////////////////////')
    print()
    while user_input != 'exit':
        user_input = input('Please, choice length of passwords between 10 or 15\nto terminate program please type -> exit\n')
        alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation    
        if user_input in '10':
            print(''.join(choice(alphabet) for char in range(10)))
        elif user_input in '15':
            print(''.join(choice(alphabet) for char in range(15)))
        elif user_input in ('exit'):
            print('By, Have fun!')
        else:
            print('Error, please try to restart programm\nand insert the valid numbers!')

if __name__ == '__main__':
    main(str)


