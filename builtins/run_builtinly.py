#! /usr/bin/env python3

"""
    Usages:
    ./run_builtinly.py                          (reads out the entire config
                                                dict)
    ./run_builtinly.py  that_key                (reads out the value associated
                                                with a particular key from
                                                the config dict)
    ./run_builtinly.py  this_key this_value    (sets this_key and this_value
                                                in the dict)
"""

import sys
from builtinly import ConfigDict

app_conf = ConfigDict('app.cfg')

if len(sys.argv) == 3:
    key = sys.argv[1]
    value = sys.argv[2]
    print("Writing data: {0} {1}".format(key, value))
    app_conf[key] = value
elif len(sys.argv) == 2:
    print("Reading a value:")
    key = sys.argv[1]
    print('The value for {0} is {1}'.format(sys.argv[1], app_conf[key]))
else:
    print("Keys/Values:")
    for key in app_conf.keys():
        print("   {0} = {1}".format(key, app_conf[key]))
