# -*- coding: utf-8 -*-
# filename: function.py


import os
import sys


def GetParentDir():
    path = os.path.dirname(os.path.realpath(sys.argv[0]))
    return os.path.dirname(path)
    
