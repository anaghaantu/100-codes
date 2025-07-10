from fractions import Fraction
n1=int(input("enter the numerator1:"))
n2=int(input("enter the numerator2:"))
d1=int(input("enter the denominator1:"))
d2=int(input("enter the denominator2:"))
f1 = Fraction(n1,d1)
f2 = Fraction(n2,d2)
sum = f1+f2
print(sum)
