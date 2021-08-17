#Compound Interest
P=eval(input('Enter Principal Amount:'))
R=eval(input('Enter Rate of Interest/Unit Time period:'))
T=eval(input('Enter time period:'))

CI= P*(1 + R/100)**T-P
print('Compund Interest:',CI)