# to convert a csv file in to data base

import csv
import sqlite3
#id,name,occupation,salary
conn = sqlite3.connect('bar.db')
cursor = conn.cursor()

cursor.execute('''create table employee 
                (id int,
                name text,
                occupation text,
                salary int);''')

file = open("s.csv")
v = csv.reader(file)
cursor.executemany('''insert into employee
                    (id,name,occupation,salary)
                    values(?,?,?,?)''',v)

cursor.execute("select * from employee")
z = cursor.fetchall()
for i in z:
    print(i[0])
    print(i[2])
    print(i[3])