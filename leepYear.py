def isLeap(year):
    if (year % 4):
        if (year % 100) == 0:
            return False
        if (year % 400) == 0:
            return True
        return False
    else:
        return False


year = int(input())

print(isLeap(year))


