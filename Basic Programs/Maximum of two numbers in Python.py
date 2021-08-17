#Using if condition
a=eval(input("Enter 1st Number:"))
b=eval(input("Enter 2nd Number:"))

if a<b:
	print('{} is greater than {}'.format(b,a))
elif a==b:
	print('{} is equal to {}'.format(a,b))
else:
	print('{} is less than {}'.format(b,a))


#Using ternary operator:
a=eval(input("Enter 1st Number:"))
b=eval(input("Enter 2nd Number:"))
print("Both the numbers are equal" if a==b else " a is greater than b" if a>b else "b is greater than a")


