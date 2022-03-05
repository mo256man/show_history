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

def get_history():

    # Chromeの履歴ファイル
    user_path = os.environ["LOCALAPPDATA"]
    db = user_path + r"\Google\Chrome\User Data\Default\History"
    db_copy = db + "_copy"

    # Historyファイルをコピーする　その前に既存のコピーがあれば消す
    if os.path.exists(db_copy):
        os.remove(db_copy)
    shutil.copyfile(db, db_copy)

    words = ""
    with closing(sqlite3.connect(db_copy)) as conn:
        c = conn.cursor()
        sqls = ["select term from keyword_search_terms", "select title from urls"]
        sqls = ["select term from keyword_search_terms"]
        for sql in sqls:
            recordset = c.execute(sql)
            for row in recordset:
                words += " " + row[0]

    # URLデコードする
    words = urllib.parse.unquote(words)

    # 全角スペースを半角スペースにする
    words.replace("　", " ")

    return words

if __name__ == "__main__":
    words = get_history()
    print(words)