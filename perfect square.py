import math
n = int(input("enter a no:"))
if math.floor(math.sqrt(n))==math.ceil(math.sqrt(n)):
    print("perfect square")
else:
    print("not a perfect square")
