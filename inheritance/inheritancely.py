"""
Challenge: Implement a library exposing two interfaces, CSVFormatter and
           LogFormatter, borrowing heavily from OOP(Inheritance) to achieve a
           brief and maintainable solution.
"""
import abc


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, writer):
        self.writer = writer

    @abc.abstractmethod
    def write(self):
        return


class CSVFormatter(WriteFile):
    def write(self):
        pass


class LogFormatter(WriteFile):
    def write(self):
        pass
