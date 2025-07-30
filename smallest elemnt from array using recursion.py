Arr = [1, 4, 45, 6, -50, 10, 2]
n = len(Arr)
smallest = Arr[0] 
for i in range(1, n):
    if Arr[i] < smallest:
        smallest = Arr[i]

print("Greatest element:", smallest)
