x = int(input("enter the x value:"))
y = int(input("enter the y value:"))
if x>0 and y>0:
        print("FIRST QUADRANT")
elif x<0 and y>0:
        print("SECOND QUADRANT")
elif x<0 and y<0:
        print("THIRD QUADRANT")
elif x>0 and y<0:
        print("FOURTH QUADRANT")
elif x==0 and y==0:
        print("ORIGIN")
elif x!=0 and y==0:
        print("X AXIS")
elif x==0 and y!=0:
    print("Y AXIS")

