n = int(input("enter the no:"))
p =n
sum=0
while n>0:
    sum+=n%10
    n=n//10
if(p%sum==0):
    print("harshad no")
else:
    print("not harshad no")
