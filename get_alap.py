#!/usr/bin/env python3
"""Üres forrásfájl létrehozása az aktuális könyvtárban."""

import os

PY_TEMPLATE = '''#!/usr/bin/env python3


def main():
    print('Py3')

##############################################################################

if __name__ == "__main__":
    main()
'''

C_TEMPLATE = '''#include <stdio.h>

int main(void)
{
    printf("C\\n");
    return 0;
}
'''

# Új nyelv felvétele: egy új sor ide (menüpont -> (név, jelölés, fájlnév, tartalom))
LANGUAGES = {
    '1': ('Python', 'py', 'alap.py', PY_TEMPLATE),
    '2': ('C', 'c', 'alap.c', C_TEMPLATE),
    '3': ('C++', 'cpp', 'alap.cpp', C_TEMPLATE),
    '4': ('Java', 'java', 'Alap.java', C_TEMPLATE),
    '5': ('JavaScript', 'js', 'alap.js', C_TEMPLATE),
    '6': ('C#', 'cs', 'Alap.cs', C_TEMPLATE)
}


def print_menu():
    print('---------------------------')
    print('Create an empty source file')
    print('---------------------------')
    for key, (name, tag, _, _) in LANGUAGES.items():
        print(f'{key}) {name:<7}[{tag}]')
    print('q) quit')


def create_file(filename, content):
    if os.path.isfile(filename):
        print(f'Hiba: a(z) {filename} már létezik, nem írom felül!')
        return
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    if filename.endswith('.py'):
        os.chmod(filename, 0o755)
    print(f'A(z) {filename} létrejött.')


def main():
    while True:
        print_menu()
        try:
            choice = input('> ').strip().lower()
        except EOFError:
            print()
            break

        if choice == 'q':
            break
        if choice in LANGUAGES:
            _, _, filename, content = LANGUAGES[choice]
            create_file(filename, content)
        else:
            print('Ismeretlen menüpont, próbáld újra!')
        print()

if __name__ == "__main__":
    main()