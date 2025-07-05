n = int(input("enter the no:"))
sum =0
for i in range(1,n):
     if n%i==0:
         sum+=i
if n == sum:
    print("perfect no")
else:
    print("not a perfect no")
