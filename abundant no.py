n = int(input("enter the no:"))
sum =1
for i in range(2,n):
    if n%i==0:
        sum +=i
if sum >n:
    print("abundant no:")
else:
    print("not abundant no")
