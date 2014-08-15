import sqlite3

conn = sqlite3.connect('locker.db')

conn.execute('''CREATE TABLE IF NOT EXIST cells(
cellid INTEGER PRIMARY KEY,
lock CHAR,
port CHAR,
state BOOL,
key CHAR,
path CHAR
);''')
conn.execute('''CREATE TABLE IF NOT EXIST log(
logid INTEGER PRIMARY KEY,
cell INT,
action BOOL,
timestamp FLOAT,
key CHAR,
FOREIGN KEY(cell) REFERENCES cells(cellid)
);
''')
# test section
for i in [1,2,3]:
    conn.execute('''INSERT INTO cells VALUES(NULL, 'test','test',0,'test','test');''')
conn.commit()
conn.close()
