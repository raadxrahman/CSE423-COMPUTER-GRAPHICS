#if -1 > m > 1 , x_(k+1) = x_k + 1 , y_(k+1) = y_k + m
#else. y_(k+1) = y_k + 1, x_(k+1) = x_k + 1/m

x0 = int(input("Enter x0: "))
y0 = int(input("Enter y0: "))
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

slope_m = (y1-y0)/(x1-x0)

print("Slope = " + str(slope_m))
if 1 > slope_m > -1:
    for x in range(x0,x1):
        x0 = x0+1
        y0 = y0+slope_m
        print(x0, round(y0))
else: 
    for x in range(y0,y1):
        y0 = y0+1
        x0 = x0+(1/slope_m)
        print(round(x0), y0)
