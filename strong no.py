n = int(input("enter the number:"))
number = n
total =0
def factorial(n):
             fact =1
             if n<0:
                 print("no factorial")
             else:
                for i in range(1,n+1):
                               fact = fact*i
                return fact

while n>0:
    digit = n%10
    total +=factorial(digit)
    n //=10
if total == number:
    print("strong no")
else:
    print("not strong no")
