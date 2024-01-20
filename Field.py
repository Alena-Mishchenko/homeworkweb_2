from abc import ABC, abstractmethod


class Field(ABC):

    @abstractmethod
    def __getitem__(self):
        pass


