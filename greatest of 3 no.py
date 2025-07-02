n1 = int(input("enter the no:"))
n2 = int(input("enter the no:"))
n3 = int(input("enter the no:"))
max = n2 if n2>n1 else n1
max = n3 if n3>max else n2
print(max)
