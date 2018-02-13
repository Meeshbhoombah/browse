# -*- encoding: utf-8 -*-
"""
list_tables.py

Collects data from sources (Wakatime, Browser History) and creates workable, cleaned, files from
the sources.
"""

import csv 
import sqlite3
import os

# sqlite database with Chrome browsing history
CHROME_HISTORY_SRC = "/Users/rohan/Library/Application Support/Google/Chrome/Default/Login Data"

# connect to History database
conn = sqlite3.connect(CHROME_HISTORY_SRC)
    
# create a cursor
cursor = conn.cursor()

"""
TABLES
"""
for row in cursor.execute("SELECT name FROM sqlite_master WHERE type='table';"):
    print(row)
