def isLeap(year):
    if (year % 4 == 0):
        if (year % 100) == 0:
            if (year % 400) == 0:
                #print(year)
                return True
            else:
                return False
        else:
            return True
    else:
        return False

                

year = int(input())

print(isLeap(year))


