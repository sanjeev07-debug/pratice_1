#  For the list items, filter all elements starting with hand and ending with at most one more character or le.
# #items = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']
import re
items  = ['handed', 'hand', 'handled', 'handy', 'unhand', 'hands', 'handle']
x = re.findall("^han.le$",items)
print(x)
