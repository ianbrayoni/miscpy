#! /usr/bin/env python3

"""
Leverage the convenience of a dictionary to power a configuration file,
which is simply a file of key-value pairs.

A configuration file is used quite often in programming shops to hold
values that don't belong in the Python script itself.
Values like SQL queries, email addresses, and other configurable values
should be stored outside of the script, because they may change when the
code itself doesn't need to be changed.

The structre of a config file could take many forms, and one of them is
a simple key=value syntax, with one key/value pair per line.
This is simple and straightforward, so we'll use it.

What's great about using a built-in structure like a dictionary as
the interface to a configuration file is that any Python programmer will
immediately know how to use it.  The instructions are so simple you almost
don't need documentation:
    "create a new ConfigDict object, then read and write keys and
    values as desired" -- that's it.


Our config file should looks like this:

    sql_query=SELECT this FROM that WHERE condition
    email_to=me@mydomain.com
    num_retries=5

"""


class ConfigKeyError(Exception):
    """
    Custom Error and Exception handling class
    """

    def __init__(self, this, key):
        self.key = key
        self.keys = this.keys()

    def __str__(self):
        return "Key '{0}' not found. Available keys: ({1})".format(
            self.key,
            ', '.join(self.keys)
        )


class ConfigDict(dict):
    """
    Class implementing interface to a configuration file.
    """

    def __init__(self, filename):
        self._filename = filename

        try:
            open(self._filename, 'w').close()
        except IOError:
            raise IOError('arg to ConfigDict must be a valid pathname')

        with open(self._filename) as file_handler:
            for line in file_handler:
                line = line.rstrip()
                key, value = line.split('=', 1)
                dict.__setitem__(self, key, value)

    def __getitem__(self, key):
        if key not in self:
            raise ConfigKeyError(self, key)
        return dict.__getitem__(self, key)

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        with open(self._filename, 'w') as file_handler:
            for key, value in self.items():
                file_handler.write('{0}={1}\n'.format(key, value))


