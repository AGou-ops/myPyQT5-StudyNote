import sqlite3
from databaseEx.createTabCol import create

conn = sqlite3.connect('students.db')

c = conn.cursor()

c.execute('''CREATE TABLE SCHOOL (ID INT PRIMARY KEY  NOT NULL,
                                  NAME           TEXT NOT NULL, 
                                  AGE            TEXT NOT NULL,
                                  ADDRESS        CHAR(50),
                                  MARKS          INT); ''')


c.close()
conn.commit()
conn.close()
