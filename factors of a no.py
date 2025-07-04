n = int(input("enter the number:"))
print("factors are:")

def factors(n):
    i =1
    while i<=n:
        if (n%i==0):
            print(i)
        i = i+1
factors(n)  
