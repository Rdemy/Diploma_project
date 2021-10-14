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


class BoardSpider:
    def __init__(self):
        self.con = sqlite3.connect('boards.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS boards(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        socket TEXT,
        chipset TEXT,
        memory_board TEXT,
        memory_slots TEXT,
        memory_value TEXT,
        waranty_board TEXT
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO boards VALUES (?,?,?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['socket'],
            item['chipset'],
            item['memory_board'],
            item['memory_slots'],
            item['memory_value'],
            item['waranty_board']
        ))
        self.con.commit()
        return item


class VideoSpider:
    def __init__(self):
        self.con = sqlite3.connect('videocards.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS videocards(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        brand TEXT,
        video_memory_type TEXT,
        video_memory_value TEXT,
        dram TEXT,
        max_video_resolution TEXT,
        waranty_video TEXT,
        freq_video
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO videocards VALUES (?,?,?,?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['brand'],
            item['video_memory_type'],
            item['video_memory_value'],
            item['dram'],
            item['max_video_resolution'],
            item['waranty_video'],
            item['freq_video']
        ))
        self.con.commit()
        return item


class RAMSpider:
    def __init__(self):
        self.con = sqlite3.connect('RAM.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS RAM(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        RAM_memory_type TEXT,
        RAM_memory_value TEXT,
        waranty_RAM TEXT
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO RAM VALUES (?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['RAM_memory_type'],
            item['RAM_memory_value'],
            item['waranty_RAM']
        ))
        self.con.commit()
        return item


class HDDSpider:
    def __init__(self):
        self.con = sqlite3.connect('HDD.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS HDD(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        HDD_model TEXT,
        speed TEXT,
        HDD_memory_value TEXT,
        waranty_HDD TEXT
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO HDD VALUES (?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['HDD_model'],
            item['speed'],
            item['HDD_memory_value'],
            item['waranty_HDD']
        ))
        self.con.commit()
        return item


class SDDSpider:
    def __init__(self):
        self.con = sqlite3.connect('SSD.db')
        self.cur = self.con.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS SSD(
        name TEXT PRIMARY KEY,
        price REAL ,
        rating REAL,
        commentary REAL,
        SSD_model TEXT,
        SSD_speed TEXT,
        SSD_memory_value TEXT,
        waranty_SSD TEXT
        )""")

    def process_item(self, item, spider):
        for field in item.fields:
            item.setdefault(field, 'NULL')
        self.cur.execute("""INSERT OR IGNORE INTO SSD VALUES (?,?,?,?,?,?,?,?)""", (
            item['name'],
            item['price'],
            item['rating'],
            item['commentary'],
            item['SSD_model'],
            item['SSD_speed'],
            item['SSD_memory_value'],
            item['waranty_SSD']
        ))
        self.con.commit()
        return item