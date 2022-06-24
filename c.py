# Write a Python program to extract urls from text file using regular expression.


import re

x = '''Now a days you can learn almost anything by just visiting http://www.google.in. But if you are completely new to computers or internet then first you need to leanr those fundamentals. Next
you can visit a good e-learning site like https://www.tutorialspoint.com to learn further on a variety of subjects.'''
# y=' http://www.google.com  https://www.tutorialspoint.com'
f = re.findall(r"\bhttps?://\w+.\w+.\w{2,3}\b",x) #use findall
print(f)