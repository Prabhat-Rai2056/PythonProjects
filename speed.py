#To check the speed of driver

def speed(s):
    d = 0
    if s < 70:
        print("ok")
    else:
        d += ((s-75) / 5) + 1
        print("your demerit point is :", d)
        if d > 12:
            print("licence suspended")
p = int(input("enter the speed of car:"))
speed(p)
