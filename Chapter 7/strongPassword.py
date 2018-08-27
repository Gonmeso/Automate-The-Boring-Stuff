#! python3
# strongPassword.py - Checks wether a password is strong enough

import re

passwords = ['hola', 'adios', 'Passwor1', 'lowerstring',
            'UPPERSTRING', '123456789', '', 'Qwertyui12']

passRegex = re.compile(r'''(
                        ^
                        (?=.*[A-Z])
                        (?=.*[a-z])
                        (?=.*[0-9])
                        .{8,}
                        $
                        )''', re.VERBOSE)

for password in passwords:

    result = passRegex.search(password)
    if result == None:
        print('The password {} is not strong enough'.format(password))
    else:
        print('Password too stronk')
