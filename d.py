import re

d = '''
    hi there this is svuppala5@gitam.in
    and kdanthul2@gitam.in welcome to python 
    class'''
x = re.findall("\S+@\S+",d)
print(x)