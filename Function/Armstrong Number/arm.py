def armstrong(num):
    length = len(str(num))
    s=0
    while(num>0):
        d=num%10
        s=s+d**length
        num=num//10
    return s
