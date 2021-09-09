#Midpoint Line Algorithm

def midpointline(x0,y0,x1,y1):
    dx = x1 - x0
    dy = y1 - y0

    d_init = (2*dy) - dx
    d = d_init
    while x0!=x1 and y0!= y1:
        print(x0,y0)
        if d > 0:
            x0 += 1
            y0 += 1
            d += 2*(dy - dx)
        else:
            x0 += 1
            d += 2*dy
    print(x0,y0)

def slope(x0,y0,x1,y1):
    slope_m = (y1-y0)/(x1-x0)
    print("Slope = " + str(slope_m))
    if 0 < slope_m < 1:
        midpointline(x0,y0,x1,y1)
    else:
        print("Slope not within 0 and 1")



if __name__ == '__main__':
    x0 = int(input("Enter x0: "))
    y0 = int(input("Enter y0: "))
    x1 = int(input("Enter x1: "))
    y1 = int(input("Enter y1: "))
    slope(x0,y0,x1,y1)

