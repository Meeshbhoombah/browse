# -*- encoding: utf-8 -*-
"""
analysis.py

Reads in text file containing formatted history data generated from Google Chrome browsing 
history and creates a pie chart of most popular sites
"""

from urlparse import urlparse
import matplotlib.pyplot as plt
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

# Aggregrate domains
site_frequencies = data.url.value_counts().to_frame()

# Make the domain a column
site_frequencies.reset_index(level=0, inplace=True)

# Rename columns to appropriate names
site_frequencies.columns = ['domain', 'count']

# Display top 2
site_frequencies.head(2)

# Create a pie chart
topN = 20
plt.figure(1, figsize=(10,10))
plt.title('Top $n Sites Visited'.replace('$n', str(topN)))
pie_data = site_frequencies['count'].head(topN).tolist()
pie_labels = None
pie_labels = site_frequencies['domain'].head(topN).tolist()
plt.pie(pie_data, autopct='%1.1f%%', labels=pie_labels)
plt.show()

