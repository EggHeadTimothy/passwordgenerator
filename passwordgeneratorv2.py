"""
Password Generator Version 2.0
Author: Timothy Eden
Date: July 10, 2023
"""

import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special = '~!@#$%^&*()_+'
all_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+'
minimum_length = 0


def generate_password(length):
    password = ''
    if length < minimum_length:
        length = minimum_length
    types = ['upper', 'lower', 'numbers', 'special']
    random.shuffle(types)
    while len(password) < length:
        while types:
            for i in types:
                if i == 'upper':
                    index = random.randint(0, 25)
                    password += upper[index]
                    types.remove('upper')
                elif i == 'lower':
                    index = random.randint(0, 25)
                    password += lower[index]
                    types.remove('lower')
                elif i == 'numbers':
                    index = random.randint(0, 9)
                    password += numbers[index]
                    types.remove('numbers')
                elif i == 'special':
                    index = random.randint(0, 12)
                    password += special[index]
                    types.remove('special')
        index = random.randint(0, 74)
        password += all_chars[index]
    return password


def main():
    program_active = True
    print('\nWelcome to Password Generator!')
    while program_active:
        invalid_length = True
        while invalid_length:
            print('\nPlease enter the desired length for your password:')
            desired_length_str = input('LENGTH: ')
            try:
                desired_length = int(desired_length_str)
                invalid_length = False
            except:
                pass
        if desired_length < minimum_length:
            print('\nFor security reasons, your password must be at least {} characters long.'.format(minimum_length))
            print('To change the minimum length settings, go to the source code and change the value assigned to the '
                  'variable minimum_length.')
        print('\nGenerating password...')
        password = generate_password(desired_length)
        print('\nYour new password is:')
        print('\n{}'.format(password))
        print('\nEnjoy!')
        print('\nPress ENTER to continue using the Password Generator, or type \'q\' and press ENTER to quit.')
        cont = input('> ')
        if cont.lower() in ['q', 'quit', 'exit']:
            program_active = False
        else:
            pass


if __name__ == '__main__':
    main()
