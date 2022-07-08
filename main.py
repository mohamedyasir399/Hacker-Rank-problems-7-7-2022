
def valid_date(y,m,d):
    if y > 0 and m>0 and d >0:
        if m <= 12 and d < 32:
            return True
        else:
            return False
    else:
        return False
def leapYear(y,m,d):
    if y %4 == 0:
        if y % 100 == 0 and y %400 == 0:
            if m == 2 and d >29:
                return False
            else:
                return True
        elif m == 2 and d >28 :
            return False
        else:
            return True
    elif m ==2 and d >28:
        return False
    else:
        return True
def avilable(m,d):
    lst =[7,8,5,3,12,1]
    if m in lst:
        if d >31:
            print('dmc')
            return(False)
        else:
            return(True)
    else:
        if d >30:
            return(False)
        else:
            return(True)
try:
    x = input().split('/')

    num1,num2,num3 = int(x[0]),int(x[1]),int(x[2])

    if valid_date(num1,num2,num3):
        if leapYear(num1,num2,num3):
            if avilable(num2,num3):
                print(True)
            else:
                print(False)
        else:
            if avilable(num2,num3):
                print(True)cd
            else:
                print(False)
    else:
        print(False)
except:
    print(False)
