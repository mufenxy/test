def datediff(str1:str,str2:str)->int:
    """
    str1,str2 be like 'yyyy-mm-dd'
    """
    if str2>str1:
        str1,str2 = str2,str1
    str1_year = int(str1[0:4])
    str1_month = int(str1[5:7])
    str1_day = int(str1[8:])

    str2_year = int(str2[0:4])
    str2_month = int(str2[5:7])
    str2_day = int(str2[8:])

    result = 0

    result+=(str1_year-str2_year)//4*(365*3+366)
    year_yushu = (str1_year-str2_year)%4
    for i in range(year_yushu,1,-1):
        if (str1_year-i)%4==0:
            result+=366
        else:
            result+=365
    last_year = (str1_year-1)%4==0
    
    for k in range(str1_month,str2_month+13):
        curr = k
        curr%=12
        if curr in [1,3,5,7,8,10,12]:
            result+=31
        elif curr in [4,6,9,11]:
            result+=30
        else:
            result+=28
    if last_year:
        result+=1
    result+=str2_day-str1_day
    return result

def main():
    print(datediff('2025-11-15','1314-05-20'))

main()
