# -*- encoding: utf-8 -*-
"""
analysis.py

Reads in text file containing formatted history data generated from Google Chrome browsing 
history and creates a pie chart of most popular sites
"""

import pandas as pd
import numpy as np
import pprint as p

# readfile
with open('hist.txt') as f:
    content = f.readlines()

# strip whitespace on first occurance of '|'
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]

