import os
import shutil
import sqlite3
from contextlib import closing
import urllib.parse
import xml.etree.ElementTree as ET


# Chromeの履歴ファイル
user_path = os.environ["LOCALAPPDATA"]
db = user_path + r"\Google\Chrome\User Data\Default\History"
db_copy = db + "_copy"

# Historyファイルをコピーする　その前に既存のコピーがあれば消す
if os.path.exists(db_copy):
    os.remove(db_copy)
shutil.copyfile(db, db_copy)

with closing(sqlite3.connect(db_copy)) as conn:
    c = conn.cursor()

    # 例1　urlsの中を見る
    ignore_words = ["Gmail", "楽天"]
    titles = []
    sql = "select title from urls"
    recordset = c.execute(sql)
    for row in recordset:
        title = row[0]
        is_ignored = False
        for word in ignore_words:
            if word in title:
                is_ignored = True
        if not is_ignored:
            title = urllib.parse.unquote(title)     # URLデコードする
            title = title.replace("\u3000", " ")     # \u3000 -> 半角スペース
            titles.append(title)
    print(titles)
    print(len(titles))
    import sys
    sys.exit()

    # 例2　keyword_search_termsの中を見る
    search_terms = []
    sql = "select term from keyword_search_terms"
    recordset = c.execute(sql)
    for row in recordset:
        term = urllib.parse.unquote(row[0])     # URLデコードする
        term = term.replace("\u3000", " ")     # \u3000 -> 半角スペース
        search_terms.append(term)
    print(search_terms)

