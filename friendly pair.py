a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def divisor(n):
    total =0
    for i in range(1,n+1):
        if n%i==0:
           total +=i
    return total
def frindely(n1,n2):
    r1=divisor(n1)/n1
    r2 = divisor(n2)/n2
    return r1==r2
if frindely(a,b):
    print("friendly pair")
else:
    print("not friendly pair")
