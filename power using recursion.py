def power(a, b):
    ans = a
    for i in range(b - 1):
        ans = a * ans
    return ans


a = 2
b = 3
print(a, "to the power", b, "is", power(a, b))
