"""
Challenge: Implement a library exposing two interfaces, CSVFormatter and
           LogFormatter, borrowing heavily from OOP(Inheritance) to achieve a
           brief and maintainable solution.
"""
import abc
import datetime


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, writer, filename):
        self.writer = writer
        self.filename = filename
        self.value = 0

    def set_val(self, value):
        self.value = value

    def get_val(self):
        return self.value

    @abc.abstractmethod
    def write(self):
        with open(self.filename, 'w'):
            self.writer.write(self.value)
        return


class CSVFormatter(WriteFile):

    def write(self):
        pass


class LogFormatter(WriteFile):

    @staticmethod
    def date_formatter():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self):
        self.value = self.date_formatter() + '  ' + self.value + '\n'
        return super(LogFormatter, self).write(self.value)
