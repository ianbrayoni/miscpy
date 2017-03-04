#! /usr/bin/env python3

"""
    Usages:
    ./run_builtinly.py                          (reads out the entire config
                                                dict)
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

else:
    print("Reading data:")
    for key in app_conf.keys():
        print("   {0} = {1}".format(key, app_conf[key]))
