n= int(input("enter the number:"))
new=0
while n > 0:
    digit = n % 10
    new= new* 10 + digit  
    n = n// 10     

print("Reversed number:",new)


