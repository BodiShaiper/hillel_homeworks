from abc import ABC, abstractmethod


class Writer(ABC):
    @abstractmethod
    def write_file(self, text):
        pass

    @abstractmethod
    def overwrite_file(self, text):
        pass
