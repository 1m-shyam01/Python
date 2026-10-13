num1=int(input("Enter the number"))
x=len(str(num1))
pow=num1**2
if(x==1):
    rem=pow%10
    if(rem==num1):
        print("This is an automorphic number")
    else:
        print("This is not a automorphic number")
if(x==2):
    rem=pow%100
    if(rem==num1):
        print("This is an automorphic number")
    else:
        print("This is not a automorphic number")
if(x==3):
    rem=pow%1000
    if(rem==num1):
        print("This is an automorphic number")
    else:
        print("This is not a automorphic number")