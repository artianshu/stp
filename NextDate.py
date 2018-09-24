def isLeapYear(year):
    if year % 4 == 0:
        if year % 100==0:
            if year % 400==0:
                return 1
        else:
            return 1
    else:
        return 0


day = int(input("Enter day:"))
mon = int(input("Enter mon:"))
year = int(input("Enter Year:"))

thirty = [4, 6, 9, 11]
thirtyOne = [1, 3, 5, 7, 8, 10, 12]
incrMon = 0
incrYear = 0
isLeap = isLeapYear(year)
flag = 0
if (mon in thirty and day > 30) or (mon in thirtyOne and day > 31) or day <= 0 or mon <= 0 or mon > 12:
    flag = 1
else:
    if (day == 30 and (mon in thirty)) or (day == 31 and (mon in thirtyOne)):
        nxtDay = 1
        incrMon = 1
    else:
        nxtDay = day + 1
        incrMon=0

    if isLeap==1 and mon==2 and day==28:
        nxtDay=day+1
        incrMon=0

    elif isLeap==1 and mon==2 and day==29:
        nxtDay=1
        incrMon=1

    elif isLeap == 0 and mon==2 and day==28:
        nxtDay=1
        incrMon=1

    if incrMon==1 and mon==12:
        nxtMon=1
        incrYear=1
    elif incrMon==0:
        nxtMon=mon
    else:
        nxtMon=mon+1

    if incrYear==1:
        nxtYear=year+1
    else:
        nxtYear=year
if flag ==1:
    print("Invalid Date")
else:
    print("Next Day")
    print("Day:",nxtDay)
    print("Mon:",nxtMon)
    print("Year:",nxtYear)




