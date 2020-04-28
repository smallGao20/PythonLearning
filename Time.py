import  time

def GetNowTime():
    return  time.strftime("%Y %m %d %H:%M:%S",time.localtime())

def SculateTime(d,h,m,s):
    nowtime = GetNowTime()
    Y1 = int(nowtime[0])*1000 + int(nowtime[1])*100 +  int(nowtime[2])*10 + int(nowtime[3])
    Mo1 = int(nowtime[5])*10 + int(nowtime[6])
    D1 = int(nowtime[8])*10 + int(nowtime[9])
    H1 = int(nowtime[11])*10 + int(nowtime[12])
    M1 = int(nowtime[14])*10 + int(nowtime[15])
    S1 = int(nowtime[17])*10 + int(nowtime[18])
    print("当前时间",Y1,"年",Mo1,"月",D1,"日")
    print("    \t",H1,":",M1,":",S1)
    ss = 0
    mm = 0
    hh = 0

    if S1 + s >= 60:
        ss = int ((S1 + s)/60)
        S1 = (S1 + s)%60
    else:
        S1 = S1 + s

    if M1 + m + ss >= 60:
        mm = int ((M1 + m + ss)/60)
        M1 = (M1 + m + ss)%60
    else:
        M1 = M1 + m + ss

    if H1 + h + mm >= 24:
        hh = int((h + mm + H1)/24)
        H1 = (h + mm + H1)%24
    else:
        H1 = h + mm + H1
    # print("hh:",hh," d:",d," D1:",D1)
    hh = hh + d + D1
    # hh 算是一个总天数（包含当月已过天数)
    # print("WorkDay After ",hh - D1," day")

    mo = Mo1

    while( hh ):
        # print("D1 = ",D1,"hh = ",hh,"mo = ",mo)
        if (mo == 1 or mo == 3 or mo ==5 or mo == 7 or mo == 8 or mo == 10 or mo == 12):
            if hh > 31:
                hh = hh - 31
                D1 = 1
                # 此处赘述D1 = 1 略显多余，因为以后可以直接使用hh代替剩余天数，但可以使代码逻辑清晰
                mo += 1

            else:
                D1 = hh
                hh = 0

        elif (mo == 4 or mo == 6 or mo == 9 or mo == 11):
            if hh > 30:
                hh = hh - 30
                D1 = 1
                mo += 1

            else:
                D1 = hh
                hh = 0

        elif (mo == 2 and ((Y1%100 != 0 and Y1%4 ==0 ) or (Y1%400==0))):
            if hh > 29:
                hh = hh - 29
                D1 = 1
                mo += 1

            else:
                D1 = hh
                hh = 0

        else:
            if hh > 28:
                hh = hh -28
                D1 = 1
                mo += 1

            else:
                D1 = hh
                hh = 0


        if( mo > 12):
            Y1 = Y1 + 1
            mo = 1

    print("Data ",Y1,"年",mo,"月",D1,"日","\n    \t",H1,":",M1,":",S1)

def GetInputTime():
    strd = input("Enter Time of Day:")
    strh = input("Enter Time of Hour:")
    strm = input("Enter Time of Mimute:")
    strs = input("Enter Time of Second:")

    d = int(strd)
    h = int(strh)
    m = int(strm)
    s = int(strs)
    print("推算时长",d,"天", h, "小时", m, "分", s,"秒")
    SculateTime(d,h,m,s)

GetInputTime()

# readme
# 此篇程序用于计算给定时间后的日期和时间（精确到秒，但是秒必须要填写），此篇程序有诸多有待修改之处例如月份与年的计算是代码冗余量大等等。
