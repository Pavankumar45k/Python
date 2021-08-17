a=eval(input("Enter a number to check it is Armstrong or not:"))
print(a)
sum=0
temp=a
while temp > 0:
    digit = temp % 10
    sum = sum+digit ** 3
    temp //= 10
if a == sum:
    print(a,"is an Armstrong number")
else:
    print(a,"is not an Armstrong number")
