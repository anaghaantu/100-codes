#AMSTRONG NO
n = int(input("enter the number:"))
num = n
sum =0
lenght = len(str(n))
while n>0:
    digit = int(n%10)
    sum =sum + pow(digit,lenght)
    n = n/10
if sum == num:
    print("amstrong no.")
else :
    print("not amstrong no.")
   
