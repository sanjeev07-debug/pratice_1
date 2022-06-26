import re 

password = "Sanjeev@35538"
x = re.complie("^(?=.*[a-z])(?=.+[A-Z])(?=.*\d)(?=*[@$!%#?&])[A-Za-z\d@&!#%*?&]{8,20}$")
mat = re.search(x,password)
if mat:
	print("wow! it is a valid passcode")
else:
	print("no it is not a valid passcode")