
def factorial(num):
    fact =1
    for i in range(1,num+1):
        fact = fact*i
    return fact
n = int(input("no of people searching for the seat:"))
r = int(input("no of remaining seats:"))
factorial(n)
factorial(n-r)
P = factorial(n)//factorial(n-r)
print(P)

    
