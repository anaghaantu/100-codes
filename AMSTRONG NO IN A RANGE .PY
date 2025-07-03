
low = int(input("enter the number:"))
high = int(input("enter the number:"))
for n in range(low,high+1):
                sum =0
                lenght = len(str(n))
                temp = n
                while temp!=0:
                    
                       digit = int(temp%10)
                       sum =sum + pow(digit,lenght)
                       temp = temp/10
                if sum == n:
                        print(n)
    
