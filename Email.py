from Field import Field
import re


class Email(Field):

    def __init__(self, value=''):
        while True:

            if value:
                self.value = value
            else:
                self.value = input("Email: ")
            try:
                if re.match('^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$', self.value) or self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect email! Please provide correct email.')

    def __getitem__(self):
        return self.value
