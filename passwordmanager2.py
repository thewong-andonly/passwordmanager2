import secrets
import csv
import string
import hashlib
import os

# Ver 1.0, base version
# Ver 1.1, added write to text file
# Ver 1.21, formatted code to be neater
# Ver 1.22, added loop

# Ver 2.1, uses secrets instead of random

ver = ('2.1')
print(f'Hello, welcome to password manager {ver}.')


def passwordmanager():
    website = input('What website is this for?: ')
    username = input(f'What is the username for {website}?: ')
    passlength = input(
        'How many characters would you like your password to be?: ')

    passchars = int(passlength)
    alphabet = string.ascii_letters + string.digits + string.punctuation
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(passchars))
        if (any(chars.islower() for chars in password)
                and any(chars.isupper() for chars in password)
                and sum(chars.isdigit() for chars in password) >= 3
                and sum(not chars.isalnum() for chars in password) == 2):
            print(f'Your password for {website} is {password}')
            break


# save and store password as plain text
    database = open(os.path.join(os.path.expanduser(
        '~'), 'Desktop', 'testfile.txt'), 'a', newline='')
    database.write(
        f'\nWebsite: {website}\nUsername: {username}\nPassword: {password}\n')
    print('Congratulations! This has been saved to the database.')
# hash password


# program loop
    print('This has been saved to the database.  Would you like to add another? Y/N')
    addanother = input()
    if addanother == 'Y' or addanother == 'y':
        passwordmanager()
    elif addanother == 'N' or addanother == 'n':
        print(f'Thank you for using password manager {ver}!')
        input('Press any key to quit.')
        quit()
    else:
        print('Please enter Y/y or N/n.')


passwordmanager()

if __name__ == '__main__':
    main()
