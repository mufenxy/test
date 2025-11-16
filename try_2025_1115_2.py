def judge_leap(year):
    return (year %4 == 0 and year%100!=0) or (year%400==0)

def DATEDIFF_01_01(str0:str)->int:
    result = 0
    year = int(str0[0:4])
    month = int(str0[5:7])
    day = int(str0[8:])
    for i in range(year):
        result+=365
        if judge_leap(i):
            result+=1
    yushu = (year-1)%4
    for k in range(year-yushu+1,year):
        result+=365
        if judge_leap(k):
            result+=1
    for k in range(1,month):
        if k in [1,3,5,7,8,10,12]:
            result+=31
        elif k in [4,6,9,11]:
            result+=30
        else:
            result+=28
            if judge_leap(year):
                result+=1
    return result+day


def DATEDIFF(str1:str,str2:str)->int:
    """
    str1,str2 be like 'yyyy-mm-dd':
    """
    if str2>str1:
        str1,str2=str2,str1
    return DATEDIFF_01_01(str1)-DATEDIFF_01_01(str2)

def DATEADD(str0:str,nums:int)->str:
    year = int(str0[0:4])
    month = int(str0[5:7])
    day = int(str0[8:])
    for k in range(1,month):
        if k in [1,3,5,7,8,10,12]:
            nums+=31
        elif k in [4,6,9,11]:
            nums+=30
        else:
            nums+=28
            if judge_leap(year):
                nums+=1
    nums+=day
    while nums>=365:
        if judge_leap(year) and nums>365:
            nums-=366
            year+=1
        elif judge_leap(year) and nums==365:
            break
        else:
            nums-=365
            year+=1
    month = 1
    day = 1
    while nums>=31:
        if month in [1,3,5,7,8,10,12]:
            month+=1
            nums-=31
        elif month in [4,6,9,11]:
            month+=1
            nums-=30
        else:
            month+=1
            nums-=28
            if judge_leap(year):
                nums-=1
    if nums == 30:
        if month in [4,6,9,11]:
            month+=1
            nums-=30
        elif month==2:
            month+=1
            nums-=28
            if judge_leap(year):
                nums-=1
    if nums==29 and month==2:
        month+=1
        nums-=28
        if judge_leap(year):
            nums-=1
    if nums==28 and month==2 and not judge_leap(year):
        month+=1
        nums-=28
    day +=nums
    year = str(year)
    if month<10:
        month = '0'+str(month)
    else:
        month = str(month)
    if day<10:
        day = '0'+str(day)
    else:
        day = str(day)
    return year+'-'+month+'-'+day

def main():
    days = DATEDIFF('2025-11-15','1314-05-20')
    print(days)
    print(DATEADD('1314-05-20',259867))

main()
