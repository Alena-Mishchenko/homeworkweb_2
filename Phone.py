from Field import Field
import re

class Phone(Field):

    def __init__(self, value=''):
        while True:
            self.value = []
            if value:
                self.values = value
            else:
                self.values = input(
                    "Phones(+48......... or +38..........) (multiple phones can be added with space between them. +48 pattern has 9 symbols after code): ")
            try:
                for number in self.values.split(' '):
                    if re.match('^\+48\d{9}$', number) or re.match('^\\+38\d{10}$', number) or number == '':
                        self.value.append(number)
                    else:
                        raise ValueError
            except ValueError:
                print(
                    'Incorrect phone number format! Please provide correct phone number format.')
            else:
                break

    def __getitem__(self):
        return self.value
