#  For the given list, filter all elements that contains either a or w using regular expression
# #items = ['goal', 'new', 'user', 'sit', 'eat', 'dinner']
import re
t = "Python3.7 programming is a oO programming lang!"
#[ing]---Check if the string has any i, n, or g characters:
x = re.findall("[ing]", t)
print(x)