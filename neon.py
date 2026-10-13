num1=int(input("Enter the number : "))
x=len(str(num1))
res=0
pow=num1**2
for i in range(0,x+1):
    rem=pow%10
    res=res+rem
    pow=pow//10

if(res==num1):
    print("This is a neon number")
else:
    print("This is not a neon number")