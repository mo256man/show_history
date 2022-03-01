import os
import shutil
import sqlite3
from contextlib import closing
from datetime import datetime

print(os.environ)
user_path = os.environ["LOCALAPPDATA"]
db = user_path + r"\Google\Chrome\User Data\Default\History"
db_copy = db + "_copy"

if os.path.exists(db_copy):
    os.remove(db_copy)
shutil.copyfile(db, db_copy)

filePath = 'result.txt'

with closing(sqlite3.connect(db_copy)) as conn:
    c = conn.cursor()
    select_sql = "select visits.id, urls.url, urls.title, visits.visit_time, visits.from_visit from visits inner join urls on visits.url = urls.id"
    with open(filePath, mode="w", encoding="utf-8") as f:
        for row in c.execute(select_sql):
            id , url, title, visit_time, from_visit = row
            timestamp = datetime.fromtimestamp(visit_time/1000000-11644473600)
            if "Google 検索" in title:
                title = title[:-len(" - Google 検索")]
                print(title)
                f.write(f"{id}, {url}, {title}, {timestamp}, {from_visit}\n")
        f.close()

