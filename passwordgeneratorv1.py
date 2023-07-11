"""
Password Generator Version 1.0
Author: Timothy Eden
Date: July 9, 2023
"""

import random

upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '0123456789'
special = '~!@#$%^&*()_+'
all_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789~!@#$%^&*()_+'
minimum_length = 0


def gp(length):
    result = ''
    for i in range(length):
        index = random.randint(0, 74)
        result += all_chars[index]
    return result


def generate_password(length):
    if length < minimum_length:
        length = minimum_length
    result = ''
    if length >= 4:
        secure = False
        while not secure:
            result = gp(length)
            try:
                has_lowercase = False
                has_uppercase = False
                has_number = False
                has_special = False
                for character in result:
                    if character in lower:
                        has_lowercase = True
                    if character in upper:
                        has_uppercase = True
                    if character in numbers:
                        has_number = True
                    if character in special:
                        has_special = True
                assert has_lowercase and has_uppercase and has_number and has_special
                secure = True
            except AssertionError:
                pass
    else:
        result = gp(length)
    return result


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
