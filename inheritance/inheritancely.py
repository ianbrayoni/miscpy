#! /usr/bin/env python3

"""
Challenge: Implement a library exposing two interfaces, CSVFormatter and
           LogFormatter, borrowing heavily from OOP(Inheritance) to achieve a
           brief and maintainable solution.
"""

import abc
import datetime


class WriteFile(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, filename):
        self.filename = filename

    def write_line(self, text):
        with open(self.filename, 'a') as f_obj:
            f_obj.write(text + '\n')

    @abc.abstractmethod
    def write(self):
        return


class CSVFormatter(WriteFile):

    def __init__(self, filename, delimiter):
        super(CSVFormatter, self).__init__(filename)
        self.delimiter = delimiter

    def write(self, input_list):
        text = self.delimiter.join(map(str, input_list))
        self.write_line(text)


class LogFormatter(WriteFile):

    @staticmethod
    def datetime_formatter():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def write(self, input_line):
        self.write_line('{datetime}  {line}'.format(
            datetime=self.datetime_formatter(),
            line=input_line
        ))

if __name__ == "__main__":
    write_csv = CSVFormatter('text.csv', ',')
    write_log = LogFormatter('text.log')

    write_log.write("test log entry")
    write_csv.write([1, 2, 3, 4, 5])
