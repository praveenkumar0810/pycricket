import os 

chd = os.chdir(r'C:\Users\praveen\Desktop\py_ex\sample')

with open('txt1.txt','w') as fopen  :
	for i in range(1) :
		fopen.write(str(i))
	 


pwd =  os.getcwd()
print("current dir : " ,pwd)


