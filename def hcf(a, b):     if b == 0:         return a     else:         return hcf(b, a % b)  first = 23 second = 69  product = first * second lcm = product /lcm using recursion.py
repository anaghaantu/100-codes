def hcf(a, b):
    if b == 0:
        return a
    else:
        return hcf(b, a % b)

first = 23
second = 69

product = first * second
lcm = product // hcf(first, second)

print('LCM of', first, 'and', second, 'is', lcm)
