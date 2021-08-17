#Array Rotation
from array import *
n=int(input("Enter a Number to shift arrays towards left:"))
a=array('i',{11,12,13,14,15})
print("Type of a is:",type(a))

#to print array before conversion
print("\n Array Before conversion:")
for i in range(len(a)):
	print(a[i],end=' ')

# to move the array towards left by n times
for i in range(0,n):    

	#create a empty array to n no.of elements
	b= a[0]

	#move elements one by one to before index
	for j in range(0, len(a)-1):    
		a[j] =a[j+1]
	
	# move the elements in b to last index of a
	a[len(a)-1] = b

#to print array after rotation by n times
print("\n Array after rotation: ");    
for i in range(0, len(a)):    
    print(a[i],end=' ')