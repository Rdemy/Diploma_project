# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
#from itemadapter import ItemAdapter
import sqlite3


class ProceccorsSpider:
    def __init__(self):
        self.con = sqlite3.connect('processors.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS prosessors(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        cores TEXT,
        frequency TEXT,
        waranty_procs TEXT,
        proc_memory_type TEXT,
        tech_process TEXT
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO prosessors VALUES (?,?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['cores'],
            item['frequency'],
            item['waranty_procs'],
            item['proc_memory_type'],
            item['tech_process']
        ))
        self.con.commit()
        return item
