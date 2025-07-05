n1 = int(input("enter the number:"))
n2 = int(input("enter the number:"))
for i in range(1,min(n1,n2)):
   if n1%i==0 and n2%i==0:
      gcd=i
print(gcd)
