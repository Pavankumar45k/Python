from array import *
a=array('i',{78,2,3,4,5,6})
print(type(a))
for i in range(0,len(a)):
	if a[i]<=a[i+1]:
		print(a[i+1])