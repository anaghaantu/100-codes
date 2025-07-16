def primechecking(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
arr = []

for i in range(2, n // 2 + 1):
    if primechecking(i) and primechecking(n - i):
        arr.append((i, n - i))

if arr:
    print(n,"can be expressed as the sum of the following prime pairs:")
    for pair in arr:
        print(pair[0],"+",pair[1],"=",n)
else:
    print(n,"cannot be expressed as the sum of two prime numbers.")
