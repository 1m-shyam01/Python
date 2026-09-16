num1=int(input("Enter the value : "))
for i in range(1,num1+1):
    for j in range(1,num1+1):
        if (i==1 or j==1 or i==num1 or j==num1 or i==j or i+j==num1+1): print("*",end=" ")
        elif(j/2==0): print(" ",end=" ")
        else:  print(" ",end=" ")
    print()