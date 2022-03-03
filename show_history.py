import os
import shutil
import sqlite3
from contextlib import closing
from datetime import datetime
import urllib.parse
import requests
import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

user_path = os.environ["LOCALAPPDATA"]
db = user_path + r"\Google\Chrome\User Data\Default\History"
db_copy = db + "_copy"

if os.path.exists(db_copy):
    os.remove(db_copy)
shutil.copyfile(db, db_copy)

terms = ""

with closing(sqlite3.connect(db_copy)) as conn:
    c = conn.cursor()

    sqls = ["select term from keyword_search_terms", "select title from urls"]
    for sql in sqls:
        recordset = c.execute(sql)
        for row in recordset:
            terms += " " + row[0]

terms = urllib.parse.unquote(terms)

app_id = "dj00aiZpPXo5cG9DYkh6Qm93byZzPWNvbnN1bWVyc2VjcmV0Jng9YTY-"
headers = {"Content-Type": "application/json",
           "User-Agent": 'Yahoo AppID: {0}'.format(app_id)}
parameters = {"app_id": app_id,  
              "sentence": "庭には二羽ニワトリがいる。", 
              "results":"ma, uniq"}

response = requests.post("https://jlp.yahooapis.jp/MAService/V1/parse",headers=headers, data=parameters)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    print(soup)
else:
    print(f"error: status_code={response.status_code}")

pass