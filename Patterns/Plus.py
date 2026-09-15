num1=int(input("Enter the value : "))
num2=int(input("Enter the value : "))
if(num1%2==1 and num2%2==1):
    for i in range(1,num1+1):
        for j in range(1,num2+1):
            if(i==num1//2+1 or j==num2//2+1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()