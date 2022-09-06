import sqlite3
import datetime

#----------Timestamp Defining---------------
now_raw = datetime.datetime.now()
now = now_raw.strftime("%Y-%m-%d %H:%M:%S")
#--------------------------------------------

db_con = sqlite3.connect('endb.sqlite')

# Creating table for Encrypt

def create_table(db_con):
    cur = db_con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS
        endb(
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            message TEXT
        )
        
        """)
    db_con.commit()

# Inserting Data in the table

def create_entry(db_con,message):
    cur = db_con.cursor()
    cur.execute(
        """
        INSERT INTO endb (timestamp , message)
        VALUES
        (?, ?)
        """, (now, message)
    )
    db_con.commit()

# Returning a sample of data by id

def get_entry(db_con,id):
    cur = db_con.cursor()
    r = cur.execute(
        """SELECT * FROM endb WHERE id=?""",(id,)
    )
    db_con.commit()
    return r

# Returning all data

def get_entries(db_con):
    cur = db_con.cursor()
    r = cur.execute(
        """SELECT * FROM endb"""
    
    )
    db_con.commit()
    return r

def delete_entry(db_con,id):
    cur = db_con.cursor()
    cur.execute(
        """DELETE FROM endb WHERE id=?""",(id,)
    )
    db_con.commit()
