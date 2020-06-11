import sqlite3

conn = sqlite3.connect('contacts.db')

c = conn.cursor()
c.execute(''' CREATE TABLE CONTACTS (ID INT PRIMARY KEY NOT NULL ,
                                     name            text not null,  
                                     phone           int not null)
''')

c.close()
conn.commit()
conn.close()