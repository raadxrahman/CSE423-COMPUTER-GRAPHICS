global x_min, y_min, x_max, y_max


def outcode(x, y):
    bit0 = ''
    bit1 = ''
    bit2 = ''
    bit3 = ''
    if x < x_min:
        bit0 = 1
    else:
        bit0 = 0
    if x > x_max:
        bit1 = 1
    else:
        bit1 = 0
    if y < y_min:
        bit2 = 1
    else:
        bit2 = 0
    if y > y_max:
        bit3 = 1
    else:
        bit3 = 0
    code = str(bit3)+str(bit2)+str(bit1)+str(bit0)
    return code


def checkBits(bit1, bit2):
    for i in range(4):
        if bit1[i] == bit2[i] and bit1[i] == '1':
            return True

    return False


def cohen(x1, y1, x2, y2):
    oc1 = outcode(x1, y1)
    oc2 = outcode(x2, y2)
    m = (y2-y1)/(x2-x1)
    print("m:", m)
    print('--------------------------------------------------------------')
    x_1 = x1
    y_1 = y1
    x_2 = x2
    y_2 = y2
    while(True):
        print('Current Outcode 1:', oc1)
        print('Current Outcode 2:', oc2)
        if oc1 == oc2 and oc1 == "0000":
            print('Final Points: (', x_1, ",", y_1, ") , (", x_2, ",", y_2, ')')
            break
        elif(checkBits(oc1, oc2)):
            print("point completely outside")
            break
        else:
            x = x1
            y = y1
            if(oc1 != "0000"):
                if(oc1[0] == '1'):
                    y = y_max
                    x = round(x1 + 1/m*(y_max - y1))
                    print('Updated top for the first outcode')
                elif(oc1[1] == '1'):
                    y = y_min
                    x = round(x1 + 1/m*(y_min - y1))
                    print('Updated bottom for the first outcode')
                elif(oc1[2] == '1'):
                    x = x_max
                    y = round(y1 + m*(x_max - x1))
                    print('Updated right for the first outcode')
                elif(oc1[3] == '1'):
                    x = x_min
                    y = round(y1+m*(x_min-x1))
                    print('Updated left for the first outcode')
                oc1 = outcode(x, y)
                x_1 = x
                y_1 = y

            elif(oc2 != "0000"):
                x = x1
                y = y1
                if(oc2[0] == '1'):
                    y = y_max
                    x = round(x2 + 1/m*(y_max - y2))
                    print('Updated top for the second outcode')
                elif(oc2[1] == '1'):
                    y = y_min
                    x = round(x2 + 1/m*(y_min - y2))
                    print('Updated bottom for the second outcode')
                elif(oc2[2] == '1'):
                    x = x_max
                    y = round(y2 + m*(x_max - x2))
                    print('Updated right for the second outcode')
                elif(oc2[3] == '1'):
                    x = x_min
                    y = round(y2+m*(x_min-x2))
                    print('Updated left for the second outcode')
                oc2 = outcode(x, y)
                x_2 = x
                y_2 = y

            print('Updated Points: (', x_1, ",", y_1, ") , (", x_2, ",", y_2, ')')
            print('--------------------------------------------------------------')
        continue


if __name__ == "__main__":
    x_min, y_min = map(int, input("X Y Min Points:").split())
    x_max, y_max = map(int, input("X Y Max Points:").split())

    x1, y1 = map(int, input("Line Starting:").split())
    x2, y2 = map(int, input("Line Ending:").split())

    cohen(x1, y1, x2, y2)
