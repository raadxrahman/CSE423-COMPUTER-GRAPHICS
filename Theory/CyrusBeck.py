global x_min, y_min, x_max, y_max
global Te, Tl


def vectormul(a, b):
    ans = 0
    ans = a[0]*b[0]+a[1]*b[1]
    return ans


def intersection(x0, y0, x1, y1, t):
    x = x0+t*(x1-x0)
    y = y0+t*(y1-y0)
    print('Original:', x, ",", y)
    print('Rounded Value', round(x), ",", round(y))


def printer(N_D, t):
    global Tl, Te
    if(N_D > 0):
        print("| PL |", end='')
        Tl = min(Tl, t)

    elif(N_D < 0):
        print("| PE |", end='')
        Te = max(Te, t)

    elif(N_D == 0):
        print("parallel line", end='')
        return
    print("Te: ", Te, " | ", end=' ')
    print("Tl: ", Tl)


def cyrus_beck(x0, y0, x1, y1):
    D = (x1-x0, y1-y0)
    print("D: ", D[0], " ", D[1])
    N_l = (-1, 0)
    N_r = (1, 0)
    N_b = (0, -1)
    N_t = (0, 1)

    print("L | ", N_l[0], "  ", N_l[1], end=' ')
    N_L_D = vectormul(N_l, D)
    print("| N_l*D: ", N_L_D, " | ", end='')
    t = -(x0-x_min)/(x1-x0)
    # t = float("{:.2f}".format(t)) || problems in intersection calculation
    print("t: ", t, end='')
    printer(N_L_D, t)

    print("R |  ", N_r[0], "  ", N_r[1], end=" ")
    N_R_D = vectormul(N_r, D)
    print("| N_r*D: ", N_R_D, " | ", end='')
    t = -(x0-x_max)/(x1-x0)
    # t = float("{:.2f}".format(t)) || problems in intersection calculation
    print("t: ", t, end="")
    printer(N_R_D, t)

    print("B |  ", N_b[0], " ", N_b[1], end=" ")
    N_B_D = vectormul(N_b, D)
    print("| N_b*D: ", N_B_D, " | ", end='')
    t = -(y0-y_min)/(y1-y0)
    # t = float("{:.2f}".format(t)) || problems in intersection calculation
    print("t: ", t, end="")
    printer(N_B_D, t)

    print("T |  ", N_t[0], "  ", N_t[1], end=" ")
    N_T_D = vectormul(N_t, D)
    print("| N_t*D: ", N_T_D, " | ", end='')
    t = -(y0-y_max)/(y1-y0)
    # t = float("{:.2f}".format(t)) || problems in intersection calculation
    print("t: ", t, end="")
    printer(N_T_D, t)

    if(Te > Tl):
        print("Line completely outside")
    elif(Te == Tl):
        print("Clipped to a point")
    else:
        print("Clipped to a point")
        print("intersection: ")
        intersection(x0, y0, x1, y1, Te)
        print("Tl: ", Tl)
        print("intersection: ")
        intersection(x0, y0, x1, y1, Tl)


if __name__ == "__main__":
    Te = 0
    Tl = 1
    x_min, y_min = map(int, input("X Y Min Points:").split())
    x_max, y_max = map(int, input("X Y Max Points:").split())

    x1, y1 = map(int, input("Line Starting:").split())
    x2, y2 = map(int, input("Line Ending:").split())

    cyrus_beck(x1, y1, x2, y2)
