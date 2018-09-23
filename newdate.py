#Function For Leap Year return 0 in case not a leap Year
def isLeapYear(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return 1
                #print("{0} is a leap year".format(year))
            else:
                return 0
                #print("{0} is not a leap year".format(year))
        else:
            return 1
            #print("{0} is a leap year".format(year))
    else:
        return 0
        #print("{0} is not a leap year".format(year))

day=int(input("Enter day:"))
mon=int(input("Enter mon:"))
year=int(input("Enter year:"))
thirty = [2,4,6,9,11]
thirtyOne = [1,3,5,7,8,10,12]
isLeap = isLeapYear(year)
flag=0
incMon=0
incYear=0
if day > 31 or day < 1 or mon > 12 or mon < 1 :
    flag=1
elif mon in thirty and day > 30:
    flag=1
elif isLeap == 0 and mon == 2 and day > 28:
    flag=1
else :
    if (day == 30 and mon in thirty) or (day==31 and mon in thirtyOne):
        nxtDay=1
        incMon=1
    else:
        nxtDay = day + 1
    #if day == 31 and mon in thirtyOne:
    #    nxtDay=1
    #    incMon=1
    #else:
    #    nxtDay = day +1

    if incMon == 1 and mon == 12:
        nxtMon = 1
        incYear = 1
    else :
        if day == 30 or day == 31:
            nxtMon = mon + 1
        else:
            nxtMon = mon
    if incYear == 1:
        nxtYear = year +1
    else:
        nxtYear = year
    if mon == 2 and isLeap == 1 and day == 29:
        nxtDay = 1
        incMon = 0
        nxtMon = mon+1
if flag == 1 :
    print("Invalid Input")
else:
    print("Next DATE is")
    print("Day: ",nxtDay)
    print("Mon: ",nxtMon)
    print("Year: ",nxtYear)
