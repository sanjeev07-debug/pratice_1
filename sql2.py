import sqlite3

conn = sqlite3.connect("varma.db")

conn.execute('''create table student
                (roll int,
                name text,
                cgpa int);''')
print("table created")

conn.execute('''insert into student values(1,'sanju',9);''')

conn.execute('''insert into student values(2,'nam',8);''')

conn.commit()

print("table created")

c = conn.execute('''select * from student''')

for i in c:
    print("roll = ",i[0])
    print('name = ',i[1])
    print('gpa = ',i[2])



#to update the database

# conn.execute('''update student set cgpa = 8.8 where roll = 2''')

#to delete 

conn.execute('''delete from student where roll = 2''')