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

def morph(text):

    app_id = "dj00aiZpPXo5cG9DYkh6Qm93byZzPWNvbnN1bWVyc2VjcmV0Jng9YTY-"
    headers = {"Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": 'Yahoo AppID: {0}'.format(app_id)}
    parameters = {"app_id": app_id,
                "sentence": text, 
                "filter": "1|2|4|9|10", 
                "results":"ma,uniq"}

    response = requests.post("https://jlp.yahooapis.jp/MAService/V1/parse",headers=headers, data=parameters)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        word_list = [word.surface.contents[0] for word in soup.word_list]
        return word_list
    else:
        print(f"error: status_code={response.status_code}")
        return [f"error: status_code={response.status_code}"]

if __name__ == "__main__":
    filename = "hasire.txt"
    with open(filename, mode="r", encoding="utf_8") as f:
        words = f.read()
    print(words)


    words = morph(words)
    print(words)
