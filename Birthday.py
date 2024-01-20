from datetime import datetime as dt
import re
from Field import Field
from datetime import datetime


class Birthday(Field):

    def __init__(self, value=''):
        while True:
            if value:
                self.value = value
            else:
                self.value = input("Birthday date(dd/mm/YYYY): ")
            try:
                if re.match('^\d{2}/\d{2}/\d{4}$', self.value):
                    self.value = dt.strptime(self.value.strip(), "%d/%m/%Y")
                    break
                elif self.value == '':
                    break
                else:
                    raise ValueError
            except ValueError:
                print('Incorrect date! Please provide correct date format.')

    def __getitem__(self):
        return self.value
