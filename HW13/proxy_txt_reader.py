from HW13.txt_reader import TxtReader
from HW13.abstract_reader import Reader
from HW13.abstract_writer import Writer


class TxtProxyWriterReader(Reader, Writer):
    def __init__(self, file_path):
        self.__result = ''
        self.__is_actual = False
        self.__txt_reader = TxtReader(file_path)

    def read_file(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__txt_reader.read_file()
            self.__is_actual = True
            return self.__result

    def write_file(self, text):
        with open(self.__txt_reader.file_path, 'a') as file:
            file.write('\n' + text)
        self.__result = text

    def overwrite_file(self, text):
        with open(self.__txt_reader.file_path, 'w') as file:
            file.write(text)
        self.__result = text


if __name__ == '__main__':
    proxy_reader = TxtProxyWriterReader('my_file.txt')

    print(proxy_reader.read_file())
    print('\n')
    print(proxy_reader.read_file())
    proxy_reader.write_file('Some Extra line')
    # proxy_reader.overwrite_file('Totally new content')
    print(proxy_reader.read_file())
