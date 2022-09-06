import sqlite3
import datetime

#----------Timestamp Defining---------------
now_raw = datetime.datetime.now()
now = now_raw.strftime("%Y-%m-%d %H:%M:%S")
#--------------------------------------------

db_con = sqlite3.connect('db.sqlite')

# Creating table

def create_table(db_con):
    cur = db_con.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS db(
            id INTEGER PRIMARY KEY,
            timestamp TEXT,
            message TEXT
            matrix TEXT
        )
        
        """)
    db_con.commit()

# Inserting Data in the table

def create_entry(db_con,message,matrix):
    cur = db_con.cursor()
    cur.execute(
        """
        INSERT INTO db (timestamp , message, matrix)
        VALUES
        (?, ?, ?)
        """, (now, message,matrix)
    )
    db_con.commit()

# Returning a sample of data by id

def get_entry(db_con,id):
    cur = db_con.cursor()
    r = cur.execute(
        """SELECT * FROM db WHERE id=?""",(id,)
    )
    db_con.commit()
    return r

# Returning all data

def get_entries(db_con):
    cur = db_con.cursor()
    r = cur.execute(
        """SELECT * FROM db"""
    
    )
    db_con.commit()
    return r

def delete_entry(db_con,id):
    cur = db_con.cursor()
    cur.execute(
        """DELETE FROM db WHERE id=?""",(id,)
    )
    db_con.commit()
