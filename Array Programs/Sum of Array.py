#Sum of given array
import array as arr
a=arr.array('i',{10,20,30})
sum=0
for i in range(len(a)):
	if a[i]==a[len(a)-1]:
		pass
	else:
		sum=a[i]+a[i+1]
print("Sum of arary of elements",sum)

'''
#Sum of a given array using inbulit function
a=[10,20,30]
print(a)
print("sum of array of element:",sum(a))
'''