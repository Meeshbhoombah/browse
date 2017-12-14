# -*- encoding: utf-8 -*-
"""
analysis.py

Reads in text file containing formatted history data generated from Google Chrome browsing 
history and creates a pie chart of most popular sites
"""

from urlparse import urlparse
import pandas as pd
import numpy as np
import pprint as p

# readfile
with open('hist.txt') as f:
    content = f.readlines()

# strip whitespace on first occurance of '|'
raw_data = [line.split('|', 1) for line in [x.strip() for x in content]]

# dataframe - "datetime" | "url"
data = pd.DataFrame(raw_data, columns=['datetime', 'url'])

# convert to datetime elements
data.datetime = pd.to_datetime(data.datetime)

# use urllib.parse to remove info from URL, leaving only domain/subdomain
parser = lambda u: urlparse(u).netloc
data.url = data.url.apply(parser)

p.pprint(data.head(1))

