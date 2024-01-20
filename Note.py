from Field import Field


class Note(Field):
    def __init__(self, value):
        self.value = value

    def __getitem__(self):
        return self.value
