num1=int(input("Enter the value : "))
for i in range(1,num1+1):
    for j in range(1,num1+1):
        if(i==j or i+j==num1+1):
            print ("*",end=" ")
        else:
            print(" ",end=" ")
    print()