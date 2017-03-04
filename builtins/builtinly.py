#! /usr/bin/env python3

"""
Write to a config file by overriding the `dict` builtin
"""
import os


class ConfigDict(dict):

    def __init__(self, filename):
        self._filename = filename
        if os.path.isfile(self._filename):
            with open(self._filename) as file_handler:
                for line in file_handler:
                    line = line.rstrip()
                    key, value = line.split('=', 1)
                    dict.__setitem__(self, key, value)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as file_handler:
            for key, value in self.items():
                file_handler.write('{0} = {1}\n'.format(key, value))


if __name__ == "__main__":
    cc = ConfigDict('app.cfg')

    cc['database'] = 'PostgreSQL'
    cc['cache'] = 'Redis'
