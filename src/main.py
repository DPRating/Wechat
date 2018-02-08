# -*- coding: utf-8 -*-
# filename: main.py


import os
import sys
import web
import time
import pandas as pd
from handle import Handle
from initialize import GetParentDir
from initialize import Initialize

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    Initialize()
    app = web.application(urls, globals())
    app.run()
