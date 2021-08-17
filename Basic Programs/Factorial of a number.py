#using Built in function:
from math import *
a=eval(input('Enter a Number to get factorial:'))
print(factorial(a))


#factorial of a number
a= int(input("Enter a number: "))
factorial = 1
if a< 0:
   	print("Sorry, factorial does not exist for negative numbers")
elif a== 0 or a==1:
	print(" factorial of a {} is 1".format(a))
else:
	for i in range(1,a+1):
		factorial = factorial*i
		# to get the factorial of a each number till given number
		#print("The factorial of {} is".format(factorial))
print("The factorial of {} is".format(factorial))