import sqlite3


def init():
    db = sqlite3.connect('./db/content-type.db', check_same_thread=False)
    return db, db.cursor()
