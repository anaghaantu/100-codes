n = int(input("enter the number:"))
def primefactor(n):
    i =2
    while n>=i:
        if n%i ==0:
            print(i)
            n = n//i
        else:
           i = i+1
primefactor(n)
