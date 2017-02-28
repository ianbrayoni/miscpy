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

    @abc.abstractmethod
    def write(self):
        with open(self.filename, 'w'):
            self.writer.write()
        return


class CSVFormatter(WriteFile):

    def __init__(self):
        pass

    def write(self):
        pass


class LogFormatter(WriteFile):

    def __init__(self):
        pass

    @staticmethod
    def date_formatter():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self):
        pass
