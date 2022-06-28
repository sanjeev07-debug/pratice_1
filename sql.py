
import sqlite3

conn = sqlite3.connect("var.db")
conn.execute('''create table student
                (roll int,
                name text,
                gpa int);''')
print("table created")

conn.execute('''insert into student 
                values(1,"sanjeev",75.3);''')

conn.execute('''insert into student
            values(2,"varma",89.5);''')

conn.execute('''insert into student
            values(3,"jay",89.7);''')
conn.execute('''insert into student
            values(4,"may",53.90);''')

conn.commit()

print("data inserted")




#to update the datebase

x = conn.execute('''select * from student''')
for i in x:
    print("roll = ",i[0])
    print('name = ',i[1])
    