#import from csv

import csv
import sqlite3
# id,name,occupation,salary
conn = sqlite3.connect("s.db")
cursor = conn.cursor()

cursor.execute('''create table std
                (id int,
                name text,
                occupation text),
                salary int);''')

f = open("s.csv")
c = csv.reader(f)
cursor.executemany('''insert into std
                    (id,name,occupation,salary)
                    values(?,?,?,?)''',c)

cursor.execute('''select * from std''')
z = cursor.fetchall()

for i in z:
    print(i[0])