#! /usr/bin/env python3

"""
Write to a config file by overriding the `dict` builtin
"""


class ConfigDict(dict):

    def __init__(self, filename):
        self.filename = filename

    def __setitem__(self, key, value):
        return dict.__setitem__(self, key, value)

    def write(self):
        file_obj = open(self.filename, 'a')
        for self.key in self.keys():
            file_obj.write('{0} = {1}\n'.format(self.key, cc[self.key]))
        file_obj.close()

    def read(self):
        file_obj = open(self.filename, 'r')
        for line in file_obj:
            print(line)
        file_obj.close()

if __name__ == "__main__":
    cc = ConfigDict('app.cfg')

    cc['database'] = 'PostgreSQL'
    cc['cache'] = 'Redis'

    cc.write()
    cc.read()
