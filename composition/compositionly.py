#! /usr/bin/env python3

"""
Challenge: Implement a library exposing two interfaces, CSVFormatter and
           LogFormatter, borrowing heavily from OOP(Composition) to achieve a
           brief and maintainable solution.

Background: Composition vs Inheritance
           --------------------------
           Some argue that inheritance establishes dependency between parent
           and child classes hence change in one close may require a change
           in another class i.e elsewhere.

           Composition uses classes that can work together and are not related
           in any particular way hence decoupled code (code that is
           independent but interactive) hence the implementation below.

           In composition, arguably, there are fewer instances in which a
           change will affect other parts of the code compared to inheritance.
"""

import datetime


class WriteFile(object):

    def __init__(self, filename, writer):
        self.f_obj = open(filename, 'w')
        self.formatter = writer()

    def write(self, text):
        self.f_obj.write(self.formatter.format(text))
        self.f_obj.write('\n')

    def close(self):
        self.f_obj.close()


class CSVFormatter(object):

    def __init__(self):
        self.delimiter = ','

    def format(self, input_list):
        new_list = []

        for element in input_list:
            if self.delimiter in element:
                new_list.append('"{element}"'.format(element=element))
            else:
                new_list.append(element)
        return self.delimiter.join(new_list)


class LogFormatter(object):

    @staticmethod
    def datetime_formatter():
        return datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def format(self, input_text):
        return '{datetime}  {text}'.format(datetime=self.datetime_formatter(),
                                           text=input_text)

if __name__ == "__main__":

    write_csv = WriteFile('text.csv', CSVFormatter)
    write_log = WriteFile('text.log', LogFormatter)

    write_csv.write(['a', 'b,2', 'c', 'd', 'e'])
    write_log.write('Sample log entry')
