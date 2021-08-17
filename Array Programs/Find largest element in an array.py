from array import *
a=array('i',{78,2,2,-1.2011,3,4,5,6})
print(type(a))
max=a[0]
min=a[0]
for i in range(0,len(a)):
	if a[i]>max:
		max=a[i]
	else:
		min=a[i]
print("Maximum number in a Array is:",max)
print("Minimum number in a Array is:",min)
