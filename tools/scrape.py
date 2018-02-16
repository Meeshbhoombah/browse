# -*- encoding: utf-8 -*-
"""
datasets.py

Collects data from sources (Wakatime, Browser History) and creates workable, cleaned, files from
the sources.
"""

import csv 
import sqlite3
import os

# sqlite database with Chrome browsing history
CHROME_HISTORY_SRC = "/Users/rohan/Library/Application Support/Google/Chrome/Default/History"

# connect to History database
try:
    conn = sqlite3.connect(CHROME_HISTORY_SRC)
except OperationError:
    print("Cannot scrape Chrome browser history while Chrome is still open.")

# create a datasets folder
os.makedirs("datasets")
    
# create a cursor
cursor = conn.cursor()

"""
TABLES
"""
for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)

"""
SCRAPE CHROME HISTORY
"""
with open ("datasets/chrome_hist.csv", "w") as write_file:

    # query table
    results = cursor.execute("SELECT * FROM urls")

    # headers
    headers = list(map(lambda x: x[0], results.description))
    
    # create a new csv writer object
    writer = csv.writer(write_file)

    writer.writerow(headers)

    # iterate through all the rows in the urls table
    for row in results:

        # write the row (tuple)
        writer.writerow(row)

"""
SCRAPE CHROME KEYWORDS
"""
with open ("datasets/chrome_keywords.csv", "w") as write_file:

    # query table
    results = cursor.execute("SELECT * FROM keyword_search_terms")
        
    # headers
    headers = list(map(lambda x: x[0], results.description))
    
    # create a new csv writer object
    writer = csv.writer(write_file)

    writer.writerow(headers)

    # iterate through all the rows in the urls table
    for row in results:

        # write the row (tuple)
        writer.writerow(row)

