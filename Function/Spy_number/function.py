def function(num1):
    sum=0
    mul=1
    while(num1>0):
        rem=num1%10
        sum=sum+rem
        mul=mul*rem
        num1=num1//10
    if(sum==mul):
        return "this is a spy number"
    else:
        return "this is not a spy number"