# -*- coding: utf-8 -*-
# filename: main.py


import os
import sys
import web
import json
import time
import pandas as pd
from handle import Handle

urls = (
    '/', 'Handle',
)

if __name__ == '__main__':
    Initialize()
    app = web.application(urls, globals())
    app.run()
